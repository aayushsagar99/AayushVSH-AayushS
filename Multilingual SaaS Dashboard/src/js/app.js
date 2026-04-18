// Function to load and apply translations
async function changeLanguage(lang) {
  try {
    // 1. Fetch the JSON file (e.g., src/locales/en.json)
    const response = await fetch(`i18n/${lang}.json`);
    const translations = await response.json();

    // 2. Find every element with a 'data-i18n' attribute
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      
      // Use the key (like "nav.home") to find the text in our JSON
      const keys = key.split('.'); 
      let text = translations;
      keys.forEach(k => text = text[k]);

      el.textContent = text;
    });
  } catch (error) {
    console.error("Could not load language file", error);
  }
}

// Listen for when the user changes the dropdown
document.getElementById('lang-select').addEventListener('change', (e) => {
  changeLanguage(e.target.value);
});

// Load English by default when the page starts
changeLanguage('en');

const ctx = document.getElementById('salesChart').getContext('2d');
new Chart(ctx, {
    type: 'line', // You can change this to 'bar' or 'pie' later!
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            label: 'Monthly Sales ($)',
            data: [1200, 1900, 3000, 5000, 2400, 3500],
            borderColor: '#4a90e2',
            tension: 0.4,
            fill: true,
            backgroundColor: 'rgba(74, 144, 226, 0.1)'
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false }
        }
    }
});
