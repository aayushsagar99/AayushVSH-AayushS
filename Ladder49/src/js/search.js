function executeSearch() {
    const query = document.getElementById('user-input').value;
    if (!query) return;

    // Move the search bar up
    document.getElementById('app').classList.add('searching');
    
    // Show results
    const results = document.getElementById('results-area');
    results.classList.remove('hidden');

    document.getElementById('ai-text').innerText = `Here is what I found about "${query}"...`;
    
    // Fake links
    const list = document.getElementById('link-list');
    list.innerHTML = `<li><a href="#">Wikipedia: ${query}</a></li><li><a href="#">Latest News on ${query}</a></li>`;
}
