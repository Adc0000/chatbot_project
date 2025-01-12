function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="user-message"><strong>You:</strong> ${userInput}</div>`;

    // Fix the URL to match Flask's port (5001)
    fetch('http://127.0.0.1:5001/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        chatBox.innerHTML += `<div class="bot-message"><strong>Bot:</strong> ${data.response}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
        document.getElementById("user-input").value = "";
    })
    .catch(error => console.error('Error:', error));
}
