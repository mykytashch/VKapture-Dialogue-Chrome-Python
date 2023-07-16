document.addEventListener("DOMContentLoaded", function() {
  let paused = false;

  function observeChat() {
    let observer = new MutationObserver(function(mutations) {
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
