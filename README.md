# DialogMasterExtension

DialogMasterExtension is a browser extension that enables conducting dialog-based surveys. It allows users to interact with a server by transmitting chat messages and storing responses for analysis. This repository contains the necessary JavaScript code for the extension and the corresponding server-side code written in Python.

## Features

- **Message Transmission**: The main functionality of the extension is implemented through the `observeChat()` function. It observes the chat conversation and sends each new message as a response to the server for storage and analysis.

## Installation

To use the DialogMasterExtension, follow these steps:

1. Clone this repository to your local machine using Git.
2. Install the required dependencies for the server by running `pip install -r requirements.txt`.
3. Start the server by running `python server.py` in the repository's root directory.
4. Load the extension into your browser:
   - Open your browser and navigate to the extensions management page (e.g., `chrome://extensions` for Google Chrome).
   - Enable the "Developer mode" option.
   - Click on the "Load unpacked" button and select the repository's `extension` directory.
   - The extension will be loaded and ready to use.

## Usage

Once the extension is installed, you can utilize its features as follows:

1. Enter the employee ID in the designated input field.
2. Click the "Load Questions" button to load the questions for the specified employee.
3. Once the questions are loaded, the current and remaining question numbers will be displayed.
4. Start a chat conversation, and the extension will observe the chat messages.
5. When a new message is added, it will be sent as a response to the server for analysis.
6. You can use the provided buttons to pause, reset, continue, and download the history of responses.
7. The delay for sending responses can be adjusted using the "Delay" dropdown.
8. The "Send Random Message" button allows you to simulate sending a random message.

Please note that the server is configured to run on `localhost` at port `5000` by default. If needed, you can modify the server configuration in the `server.py` file.

## Technologies Used

The DialogMasterExtension utilizes the following technologies:

- JavaScript: Used for implementing the browser extension functionality.
- Python: Used for creating the server-side application.
- Flask: A web framework used for handling server requests and responses.
- SQLite: A lightweight database management system used for storing question and response data.

## Contributing

Contributions to the DialogMasterExtension project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any inquiries or questions, you can reach us at [mykytashch@hotmail.com](mailto:mykytashch@hotmail.com).

## Authors

- Mykyta Shcheholevatyi

We would like to express our gratitude to all the contributors who helped make this project possible.

Thank you for using the DialogMasterExtension!
