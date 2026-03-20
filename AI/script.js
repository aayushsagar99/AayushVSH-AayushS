const API_KEY = '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';
const chatInput = document.getElementById('chatInput');
const sendButton = document.getElementById('sendButton');
sendButton.addEventListener('click', () => handleSendMessage());
chatInput.addEventListener('keypress', event => {
    if (event.key === 'Enter') {
        handleSendMessage();
    }
})
function handleSendMessage() {
    const question = chatInput.value.trim();
    console.log(question)
}
const fetchData =
    fetch("https://openrouter.ai/api/v1/chat/completions", {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${API_KEY}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "model": "deepseek/deepseek-r1-distill-llama-70b:free",
            "messages": [
                {
                    "role": "user",
                    "content": "Introduce yourself"
                }
            ]
        })
    });
// fetchData.then(response => response.json())
//.then(data => console.log(data.choices[0].message.content)) 