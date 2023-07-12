# VKaptureDialogueChromePython

VKaptureDialogueChromePython is a browser extension that enables the transmission of messages from a chat conversation to a server. The extension facilitates dialog-based surveys by collecting and storing user responses on the server for analysis.

## Message Transmission

The primary functionality of the VKaptureDialogueChromePython is the implementation of message transmission. The extension observes the chat conversation in real-time and sends each new message to the server for storage and analysis. This allows for the seamless collection of user responses and enables efficient data processing.

The `observeChat()` function in the JavaScript code is responsible for monitoring the chat conversation. It utilizes the `MutationObserver` API to detect new message nodes added to the chat container. When a new message is detected, the extension extracts the message text and sends it to the server using the `sendResponse()` function. The server then stores the message along with relevant information such as the employee ID, question text, and processed ID.

The message transmission functionality ensures that user responses are captured accurately and promptly, providing a smooth user experience during dialog-based surveys.

## Installation

To use the DialogMasterExtension, follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python dependencies by running `pip install -r requirements.txt`.
3. Start the server by running `python server.py` in the root directory of the repository.
4. Install the browser extension:
   - Open your browser and navigate to the extensions management page (e.g., `chrome://extensions` for Google Chrome).
   - Enable "Developer mode".
   - Click on "Load unpacked" and select the `extension` directory within the cloned repository.
   - The extension will be loaded and ready to use.

## Usage

Once the extension is installed, follow these steps to use the DialogMasterExtension:

1. Enter the employee ID in the "Questionnaire #" input field.
2. Click the "OK" button to load the corresponding questionnaire from the server.
3. Select the desired delay from the "Delay" dropdown.
4. Click the "Continue" button to resume the survey or start a new survey.
5. Engage in a chat conversation, and the extension will observe and transmit new messages to the server.
6. The server stores the messages along with relevant information for analysis.
7. Use the provided buttons to pause, reset, or download the response history.
8. The status popup window displays success messages or any errors encountered during the survey process.

## Technologies Used

The DialogMasterExtension utilizes the following technologies:

- HTML: Markup language used for the extension's user interface.
- JavaScript: Programming language used for client-side functionality.
- Python: Programming language used for the server-side application.
- Flask: Python web framework used for handling server requests and responses.
- SQLite: Lightweight database management system used for storing questionnaire and response data.

## Server

The server-side application is implemented using Python and the Flask framework. It provides several endpoints for interacting with the extension:

- `/get_questions`: Retrieves the questionnaire for a specific employee ID.
- `/store_response`: Stores a user's response in the server's database.
- `/update_state`: Updates the current state of the survey for a specific employee.
- `/reset`: Resets the survey for a specific employee, clearing all responses.
- `/export`: Exports the response history for a specific employee in a downloadable format.

The server uses SQLite as the database management system for storing questionnaire and response data. The `dialog.db` file contains the necessary tables for managing the survey process.

## Contributing

Contributions to the DialogMasterExtension project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any inquiries or questions, you can reach us at [mykytashch@hotmail.com](mailto:mykytashch@hotmail.com).

## Author

- Mykyta Shcheholevatyi

We would like to express our gratitude to all the contributors who helped make this project possible.

Thank you for using the DialogMasterExtension!


