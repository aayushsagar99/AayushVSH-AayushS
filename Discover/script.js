// Sample transaction data
const transactions = [
    { date: '2023-10-01', desc: 'Starbucks Coffee', amount: '-$5.50' },
    { date: '2023-10-02', desc: 'Employer Deposit', amount: '+$1,500.00' },
    { date: '2023-10-03', desc: 'Amazon.com', amount: '-$43.00' }
];


// Function to add a new transaction
function addTransaction() {
    const date = document.getElementById('date').value;
    const desc = document.getElementById('desc').value;
    const amount = document.getElementById('amount').value;

    transactions.push({ date, desc, amount });
    renderTransactions();
}
// Function to render transactions
function renderTransactions() {
    const list = document.getElementById('transaction-list');
    list.innerHTML = transactions.map(t => `
        <tr>
            <td>${t.date}</td>
            <td>${t.desc}</td>
            <td style="color: ${t.amount.startsWith('+') ? 'green' : 'red'}">${t.amount}</td>
        </tr>
    `).join('');
}

// Initial render
document.addEventListener('DOMContentLoaded', renderTransactions);

// Mock logout functionality
document.getElementById('logout-btn').addEventListener('click', () => {
    alert("Logging out safely...");
    window.location.replace(`../logout/index.html`);
});
