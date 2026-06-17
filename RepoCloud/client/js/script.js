document.addEventListener('DOMContentLoaded', () => {
    // 1. Dynamic Navbar: Changes background when scrolling down
    const navbar = document.querySelector('.navbar');
    
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('nav-scrolled');
            } else {
                navbar.classList.remove('nav-scrolled');
            }
        });
    }

    // 2. Interactive "Connect Repository" Button
    const connectBtn = document.querySelector('.btn-large');
    
    if (connectBtn) {
        connectBtn.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Store original state
            const originalText = connectBtn.textContent;
            
            // Loading state
            connectBtn.textContent = 'Connecting...';
            connectBtn.style.opacity = '0.7';
            connectBtn.style.cursor = 'wait';
            connectBtn.disabled = true;
            
            // Simulate an API call / Connection delay (1.5 seconds)
            setTimeout(() => {
                // Success state
                connectBtn.textContent = '✓ Connected';
                connectBtn.style.backgroundColor = '#2e7d32'; // Success green
                connectBtn.style.opacity = '1';
                connectBtn.style.cursor = 'pointer';
                
                // Reset back to normal after 3 seconds
                setTimeout(() => {
                    connectBtn.textContent = originalText;
                    connectBtn.style.backgroundColor = '#1a1a1a'; // Reset to dark
                    connectBtn.disabled = false;
                }, 3000);
            }, 1500);
        });
    }

    // 3. Smooth Scrolling for future anchor links (e.g., href="#features")
    const navLinks = document.querySelectorAll('.nav-links a');
    
    navLinks.forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const target = this.getAttribute('href');
            
            // Only apply smooth scroll if it's an internal link
            if (target && target.startsWith('#') && target !== '#') {
                e.preventDefault();
                const targetElement = document.querySelector(target);
                
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', () => {
    
    // --- COMPONENT LOADER ---
    // A reusable function to fetch HTML files and inject them into containers
    function loadComponent(containerId, filePath) {
        const container = document.getElementById(containerId);
        
        if (container) {
            fetch(filePath)
                .then(response => {
                    if (!response.ok) throw new Error(`Could not load ${filePath}`);
                    return response.text();
                })
                .then(htmlData => {
                    container.innerHTML = htmlData;
                    
                    // Specific fix to make the injected navbar solid white in the dashboard
                    if (containerId === 'global-navbar-container') {
                        const nav = container.querySelector('.navbar');
                        if (nav) {
                            nav.style.background = '#ffffff';
                            nav.style.position = 'relative';
                            nav.style.borderBottom = '1px solid #e2e8f0';
                        }
                    }
                    
                    // Specific fix to shrink the massive marketing footer for the dashboard
                    if (containerId === 'global-footer-container') {
                        const footer = container.querySelector('.app-footer');
                        if (footer) {
                            footer.style.marginTop = '0';
                            footer.style.padding = '2rem 0';
                            footer.style.background = 'transparent';
                        }
                    }
                })
                .catch(error => console.error(error));
        }
    }

    // Execute the loader for both components!
    loadComponent('global-navbar-container', '../client/components/navbar.html');
    loadComponent('global-footer-container', '../client/components/footer.html');

    // ... (Keep the rest of your existing interactive JS below this) ...
});