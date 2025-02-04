# Ollama Chat Bot with Code Block Extraction

This project provides a Python-based chat client that interacts with the [Ollama](https://ollama.ai/) API. It allows you to send messages to a specified model and automatically saves any code blocks returned in the responses to separate files based on their programming language extension.

## Prerequisites

Before running this program, ensure that you have the following installed and configured:

1. **Python 3.7 or higher:**  
   Download and install from [python.org](https://www.python.org/downloads/).

2. **Python Packages:**  
   Install the required Python packages using pip:
   ```bash
   pip install requests
   ```

3. **Ollama Installation:**  
   - Ensure you have installed Ollama on your machine.  
   - Verify that the Ollama API is running on `http://127.0.0.1:11434`. If you have installed it on a different host or port, update the `API_URL` in the script accordingly.

4. **Configured Model:**  
   - Have at least one model installed in Ollama (for example, `deepseek-r1:7b`).  
   - Update the `MODEL` variable in the script if you intend to use a different model.

## Getting Started

Follow these steps to run the chat bot:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/valinux/Ollama-Chat-Bot-with-Code-Block-Extraction.git
   cd ollama-chat-bot
   ```

2. **Review and Update the Script (if needed):**

   - Open the script file (e.g., `chat_bot.py`).
   - Check that `API_URL` is set to `http://127.0.0.1:11434/api/chat`.
   - Ensure the `MODEL` variable matches the model you have installed in Ollama.
   - Modify the language extension mapping in the script if you want to support additional languages.

3. **Run the Script:**

   ```bash
   python chat_bot.py
   ```

   The terminal will display:
   ```
   Ollama Chat Bot (type 'exit' to quit)
   ------------------------------------
   You:
   ```

4. **Interacting with the Chat Bot:**

   - Type your messages and press Enter.
   - The assistant’s responses will be printed on the console.
   - Any code blocks detected in the assistant's responses will be saved locally in files (e.g., `code_output_1.py`, `code_output_2.c`, etc.), based on the language specifier provided in the code block. If no language is specified or an unrecognized language is used, the file will be saved with a `.txt` extension.

## Example Code Block in a Response

If the assistant returns a code block like this:
```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```
It will be saved locally as `code_output_1.c`.

## Troubleshooting

- **Connection Issues:**  
  If you receive an error related to the Ollama API connection (e.g., `ConnectionError`), ensure that Ollama is installed correctly and running on the specified endpoint.

- **Missing Packages:**  
  If the script complains about missing packages, double-check that you have installed all required packages using pip.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/ollama-chat-bot/issues).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
