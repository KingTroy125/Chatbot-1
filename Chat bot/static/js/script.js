document.getElementById('send-button').addEventListener('click', function() {
    var userInput = document.getElementById('user-input').value;
    document.getElementById('user-input').value = '';

    var messageDiv = document.createElement('div');
    messageDiv.textContent = 'User: ' + userInput;
    document.getElementById('messages').appendChild(messageDiv);

    fetch('/chat', {
        method: 'POST',
        body: JSON.stringify({ message: userInput }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        var botMessageDiv = document.createElement('div');
        botMessageDiv.textContent = 'Bot: ' + data.reply;
        document.getElementById('messages').appendChild(botMessageDiv);
    });
});
