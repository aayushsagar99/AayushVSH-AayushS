const form = document.getElementById('my-form');
const tableBody = document.getElementById('table-body');
const ratingSlider = document.getElementById('rating');
const ratingDisplay = document.getElementById('rating-val');

// Update slider value display
ratingSlider.oninput = () => ratingDisplay.innerText = ratingSlider.value;

// Fetch and display data
async function loadInsights() {
    try {
        const res = await fetch('http://localhost:8080/api/insights');
        const data = await res.json();
        tableBody.innerHTML = data ? data.reverse().map(row => `
            <tr><td>${row.timestamp}</td><td>${row.language}</td><td>${row.rating}/10</td></tr>
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

loadInsights(); // Initial load
