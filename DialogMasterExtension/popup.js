
// Обработчик изменения выбора задержки
document.getElementById("delaySelect").addEventListener("change", function () {
  let selectedDelay = document.getElementById("delaySelect").value;
  // Действия при изменении задержки
  console.log("Selected delay:", selectedDelay);
});


// Обработчик нажатия кнопки "ОК" для подключения к базе данных вопросов

document.getElementById("loadQuestionsButton").addEventListener("click", function () {
  let employeeID = document.getElementById("EmployeeID").value;
  let startFrom = /* получить идентификатор текущего вопроса (CurrentQuestionID) из состояния приложения */;
  fetch('http://localhost:5000/load_questions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'EmployeeID': employeeID,
      'startFrom': startFrom
    })
  })
    .then(response => response.json())
    .then(data => {
      // Обработка полученных вопросов
      console.log("Questions:", data.questions);
    })
    .catch(console.error);
});


// Обработчик нажатия кнопки "Продолжить"
document.getElementById("continueButton").addEventListener("click", function () {
  let employeeID = document.getElementById("EmployeeID").value;
  fetch('http://localhost:5000/load_state', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'EmployeeID': employeeID
    })
  })
    .then(response => response.json())
    .then(data => {
      // Обработка полученного состояния
      console.log("Current Question ID:", data.CurrentQuestionID);
      console.log("Remaining Questions:", data.RemainingQuestions);
    })
    .catch(console.error);
});


// Обработчик нажатия кнопки "Приостановить"
document.getElementById("pauseButton").addEventListener("click", function () {
  // Действия при нажатии кнопки "Приостановить"
});

// Обработчик нажатия кнопки "Начать заново"
document.getElementById("resetButton").addEventListener("click", function () {
  let employeeID = document.getElementById("EmployeeID").value;
  fetch('http://localhost:5000/reset_survey', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'EmployeeID': employeeID
    })
  })
    .then(response => {
      // Действия после сброса опроса
    })
    .catch(console.error);
});

// Обработчик нажатия кнопки "Скачать историю"
document.getElementById("downloadHistoryButton").addEventListener("click", function () {
  let employeeID = document.getElementById("EmployeeID").value;
  fetch('http://localhost:5000/download_history', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'EmployeeID': employeeID
    })
  })
    .then(response => response.blob())
    .then(blob => {
      // Создание и загрузка файла истории
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'result.txt';
      a.click();
      window.URL.revokeObjectURL(url);
    })
    .catch(console.error);
});

// Обработчик наблюдения за новыми сообщениями
document.addEventListener("DOMContentLoaded", function () {
  let paused = false;

  function observeChat() {
    let observer = new MutationObserver(function (mutations) {
      for (let mutation of mutations) {
        for (let node of mutation.addedNodes) {
          if (node.nodeType === Node.ELEMENT_NODE) {
            let messageNode = node.querySelector(".im-mess--text.wall_module._im_log_body");
            if (messageNode) {
              let userMessage = messageNode.innerText;
              if (userMessage) {
                observer.disconnect();

                fetch('http://localhost:5000/store_response', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({
                    'message': userMessage
                  })
                })
                  .then(response => {
                    console.log("Response from server:", response);
                    if (!paused) {
                      observeChat(); // Re-observe chat after sending message
                    }
                  })
                  .catch(console.error);

                break;
              }
            }
          }
        }
      }
    });

    let chatContainer = document.querySelector(".im-page--chat-body-wrap-inner-2");
    observer.observe(chatContainer, { childList: true, subtree: true });
  }

  observeChat();
});

// Обработчик нажатия кнопки "Отправить случайное сообщение"
document.getElementById("sendRandomButton").addEventListener("click", function () {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    let randomNumber = Math.floor(Math.random() * 10000000000).toString().padStart(10, "0");
    chrome.tabs.executeScript(tabs[0].id, {
      code: `
        var inputField = document.querySelector(".im_editable");
        if (inputField) {
          inputField.innerHTML = "${randomNumber}";
          var event = new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true });
          inputField.dispatchEvent(event);
        }
      `,
    });
  });
});