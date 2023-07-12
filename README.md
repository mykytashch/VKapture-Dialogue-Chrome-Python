# DialogMasterExtension

DialogMasterExtension is a browser extension that allows for conducting dialog-based surveys. It interacts with a server to load questions, send responses, and perform various survey-related actions. This repository contains the code for the extension and the server.

## Server

The server is implemented in Python using the Flask framework. It provides API endpoints for retrieving questions, storing responses, updating the survey state, resetting the survey, and exporting response data.

### Installation

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Install the required Python packages by running the following command in the repository's root directory:

```
pip install -r requirements.txt
```

### Usage

To start the server, run the following command in the repository's root directory:

```
python server.py
```

By default, the server will run on `http://localhost:5000`.

### API Endpoints

- `GET /get_questions`: Retrieves the questions for a specific employee. Requires the `EmployeeID` query parameter.

- `POST /store_response`: Stores a response from the extension. Expects a JSON payload with the following fields: `employee_id`, `question_text`, `processed_id`, and `message`.

- `POST /update_state`: Updates the current state of the survey. Expects a JSON payload with the following fields: `employee_id`, `remaining_questions`, and `current_question_id`.

- `POST /reset`: Resets the survey for a specific employee. Expects a JSON payload with the `employee_id` field.

- `GET /export`: Exports the response data for a specific employee. Requires the `employee_id` query parameter. The response data will be downloaded as a file named `result.txt`.

## Extension

The extension is implemented using JavaScript and runs in the browser. It interacts with the server to load questions, send responses, and perform survey-related actions.

### Installation

1. Open your browser and go to the extensions management page.
2. Enable the "Developer mode" option.
3. Click on the "Load unpacked" button.
4. Select the `extension` directory from this repository.

### Usage

1. Enter the employee ID in the designated input field.
2. Click the "Load Questions" button to load the questions for the specified employee.
3. Once loaded, the current and remaining question numbers will be displayed.
4. Start a chat conversation and observe the chat messages. Each new message will be sent as a response to the server.
5. Use the provided buttons to pause, reset, continue, and download the history of responses.
6. The delay for sending responses can be adjusted using the "Delay" dropdown.
7. The "Send Random Message" button can be used to simulate sending a random message.

## Contributors

- Mykyta Shcheholevatyi

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
