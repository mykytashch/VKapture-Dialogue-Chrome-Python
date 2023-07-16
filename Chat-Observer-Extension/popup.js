document.addEventListener("DOMContentLoaded", function() {
  let messages = [];

  fetch('http://localhost:5000/get_message')
    .then(response => response.json())
    .then(data => {
      messages = data.messages;
    })
    .catch(console.error);

  function sendResponseToServer(message) {
    fetch('http://localhost:5000/store_response', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        'message': message
      })
    })
      .then(response => {
        console.log("DEBUG:root:Stored response:", message);
      })
      .catch(console.error);
  }

  function observeChat() {
    let chatContainer = document.querySelector(".im-page--chat-body-wrap-inner-2");

    let observer = new MutationObserver(function(mutations) {
      for (let mutation of mutations) {
        for (let node of mutation.addedNodes) {
          if (node.nodeType === Node.ELEMENT_NODE) {
            let messageNode = node.querySelector(".im-mess--text.wall_module._im_log_body");
            if (messageNode) {
              let userMessage = messageNode.innerText;
              if (userMessage) {
                sendResponseToServer(userMessage);
              }
            }
          }
        }
      }
    });

    observer.observe(chatContainer, { childList: true, subtree: true });
  }

  observeChat();
});
