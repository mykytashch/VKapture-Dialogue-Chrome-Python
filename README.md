# DialogMasterExtension

DialogMasterExtension is a browser extension that enables the implementation of dialog-based surveys. It allows for the transmission of messages from the chat interface to a server for storage and analysis. This repository contains both the client-side JavaScript code for the extension and the server-side Python code.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Server](#server)
- [Extension](#extension)
- [License](#license)
- [Contributors](#contributors)

## Installation

To use the DialogMasterExtension, follow these steps:

1. Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/yourusername/DialogMasterExtension.git
   ```

2. Set up the server:
   - Install the required dependencies by running `pip install -r requirements.txt` in the repository's root directory.
   - Start the server by running `python server.py`.

3. Load the extension into your browser:
   - Open your browser and go to the extensions management page (e.g., `chrome://extensions` for Google Chrome).
   - Enable the "Developer mode" option.
   - Click on the "Load unpacked" button and select the repository's `extension` directory.
   - The extension should now be loaded and ready to use.

## Usage

The DialogMasterExtension facilitates dialog-based surveys through the transmission of chat messages to a server for analysis. Here's how you can use it:

1. Launch the extension by clicking on its icon in the browser's toolbar.

2. Enter the employee ID in the designated input field.

3. Click the "Load Questions" button to load the questions associated with the specified employee ID from the server.

4. Once the questions are loaded, the current question number and the remaining number of questions will be displayed.

5. Start a chat conversation in your messaging application.

6. As new chat messages are added, the extension will observe the chat and transmit each new message to the server for storage and analysis.

7. You can use the provided buttons to perform various actions:
   - "Continue" button: Resume the survey after pausing.
   - "Pause" button: Pause the survey.
   - "Reset" button: Reset the survey progress and clear all responses for the current employee.
   - "Download History" button: Export the response history for the current employee as a text file.

8. The "Delay" dropdown allows you to adjust the delay between message transmissions to the server. The default delay is set to 1 second.

9. The "Send Random Message" button is used to simulate sending a random message. This can be useful for testing and demonstration purposes.

## Server

The server-side of DialogMasterExtension is implemented in Python using the Flask framework. It provides several endpoints for handling requests from the extension:

- `/get_questions`: Retrieves the questions associated with a specific employee ID.
- `/store_response`: Stores a response message sent from the extension.
- `/update_state`: Updates the state of the survey for a specific employee.
- `/reset`: Resets the survey progress and clears all responses for a specific employee.
- `/export`: Exports the response history for a specific employee as a text file.

The server connects to a SQLite database to store and retrieve question and response data. The database file is located in the repository's root directory and is named `dialog.db`.

## Extension

The client-side of DialogMasterExtension is implemented as a browser extension using JavaScript. The main functionality of the extension is realized through the `observeChat()` function, which observes the chat conversation and sends each new message as a response to the server for storage and analysis.

The extension provides the following features:
- Loading questions for a specific employee ID.
- Sending responses to the server.
- Observing chat messages.
- Displaying status messages.
- Pausing and resuming the survey.
- Resetting the survey progress.
- Exporting the response history as a text file.
- Adjusting the delay between message transmissions.
- Simulating sending a random message.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributors

- [Mykyta Shcheholevatyi](https://github.com/mykytashch)

Contributions to this project are welcome. You can contribute by submitting issues or pull requests.
