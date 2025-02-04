import requests
import json
import re  # Regular expression module for finding code blocks

# Ollama API endpoint
API_URL = "http://127.0.0.1:11434/api/chat"

# Choose the model you have installed (e.g., llama2, mistral, etc.)
MODEL = "deepseek-r1:7b"

# Mapping from language specifier to file extension
LANGUAGE_EXTENSION_MAP = {
    "python": "py",
    "py": "py",
    "c": "c",
    "cpp": "cpp",
    "c++": "cpp",
    "java": "java",
    "javascript": "js",
    "js": "js",
    "html": "html",
    "css": "css",
    "bash": "sh",
    "shell": "sh",
    "go": "go",
    "ruby": "rb",
    "php": "php",
    # Add more mappings as needed
}

def save_code_blocks(text):
    """
    Searches for code blocks in the given text (i.e., triple-backtick sections)
    and saves each block locally using the language-specific file extension if available.
    """
    # Regex explanation:
    # - The first capturing group (\w+)? optionally matches a language specifier right after the opening backticks.
    # - The second capturing group (.*?) captures the code content non-greedily until the closing backticks.
    code_blocks = re.findall(r"```(\w+)?\n(.*?)\n```", text, re.DOTALL)
    for i, (lang, code) in enumerate(code_blocks, start=1):
        # Determine file extension based on language; default to 'txt' if not specified or unknown.
        extension = LANGUAGE_EXTENSION_MAP.get(lang.lower(), "txt") if lang else "txt"
        file_name = f"code_output_{i}.{extension}"
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(code)
            print(f"Code block saved to {file_name}")
        except Exception as e:
            print(f"Failed to save code block {i}: {e}")

def chat_with_ollama():
    # Initialize conversation history
    messages = [{
        "role": "system",
        "content": "You are a helpful assistant. Keep responses concise."
    }]
    
    print("Ollama Chat Bot (type 'exit' to quit)")
    print("------------------------------------")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            break
        
        # Add user message to history
        messages.append({"role": "user", "content": user_input})
        
        try:
            # Create the request data
            data = {
                "model": MODEL,
                "messages": messages,
                "stream": False
            }
            
            # Send POST request to Ollama
            response = requests.post(
                API_URL,
                json=data,
                headers={"Content-Type": "application/json"}
            )
            
            # Check for successful response
            if response.status_code == 200:
                response_data = response.json()
                assistant_response = response_data['message']['content']
                print(f"\nAssistant: {assistant_response}\n")
                
                # Save any code blocks from the assistant's response
                save_code_blocks(assistant_response)
                
                # Add assistant response to history
                messages.append({
                    "role": "assistant",
                    "content": assistant_response
                })
            else:
                print(f"Error: {response.status_code} - {response.text}")
                
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    chat_with_ollama()

