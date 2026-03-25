const form = document.getElementById('my-form');
const tableBody = document.getElementById('table-body');
const ratingSlider = document.getElementById('rating');
const ratingDisplay = document.getElementById('rating-val');

// Update slider value display
ratingSlider.oninput = () => ratingDisplay.innerText = ratingSlider.value;

// Fetch and display data
// Function to handle the actual copying
async function copyToClipboard(text, btn) {
    await navigator.clipboard.writeText(text);
    const originalText = btn.innerText;
    btn.innerText = "Saved!";
    btn.classList.add('copied');
    
    setTimeout(() => {
        btn.innerText = originalText;
        btn.classList.remove('copied');
    }, 1500);
}


async function loadInsights() {
    try {
        const res = await fetch('http://localhost:8080/api/insights');
        const data = await res.json();
        
        tableBody.innerHTML = data ? data.reverse().map(row => `
            <tr>
                <td>${row.timestamp}</td>
                <td>${row.language}</td>
                <td>${row.rating}/10</td>
                <td style="text-align: right;">
                    <button class="copy-btn" onclick="copyToClipboard('${row.language}', this)">Copy</button>
                </td>
            </tr>
        `).join('') : "";
    } catch (e) { tableBody.innerHTML = ""; }
}


// Handle Submit
form.onsubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    await fetch('http://localhost:8080/submit', {
        method: 'POST',
        body: formData,
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
    });
    form.reset();
    ratingDisplay.innerText = "5";
    loadInsights();
};

// Handle Clear
document.getElementById('clear-btn').onclick = async () => {
    if(confirm("Wipe all history?")) {
        await fetch('http://localhost:8080/api/clear');
        loadInsights();
    }
};

const themeToggle = document.getElementById('theme-toggle');

themeToggle.onclick = () => {
    document.body.classList.toggle('light-mode');
    themeToggle.innerText = document.body.classList.contains('light-mode') ? "☀️" : "🌙";
};


loadInsights(); // Initial load
