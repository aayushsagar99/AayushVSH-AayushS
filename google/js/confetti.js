document.addEventListener('DOMContentLoaded', () => {

    const facts = [
        "🧱 Google's first server was housed in LEGO bricks!",
        "🐶 Google's first company dog was named Yoshka.",
        "🐐 Google rents goats to 'mow' the lawns at HQ!",
        "👕 The first 'Google Doodle' was a Burning Man figure.",
        "📉 In 1999, the founders tried to sell Google for $750k."
    ];
    const googleColors = ["#4285F4", "#EA4335", "#FBBC05", "#34A853"];
    let index = 0;

    const btn = document.getElementById('final-portal');

    // 1. BUILT-IN CONFETTI (No external library needed!)
    function fireConfetti() {
        for (let i = 0; i < 50; i++) {
            const confetti = document.createElement('div');
            confetti.innerText = "🎉";
            confetti.style.position = 'fixed';
            confetti.style.left = Math.random() * 100 + 'vw';
            confetti.style.top = '100vh';
            confetti.style.fontSize = Math.random() * 20 + 20 + 'px';
            confetti.style.zIndex = '999';
            confetti.style.pointerEvents = 'none';
            confetti.style.transition = 'transform ' + (Math.random() * 2 + 1) + 's linear, opacity 2s';
            
            document.body.appendChild(confetti);

            // Animate up and fade out
            setTimeout(() => {
                confetti.style.transform = `translateY(-120vh) rotate(${Math.random() * 360}deg)`;
                confetti.style.opacity = '0';
            }, 10);

            // Clean up
            setTimeout(() => confetti.remove(), 3000);
        }
    }

    // 2. CLICK ACTION
    btn.addEventListener('click', () => {
        // Trigger the internal confetti
        fireConfetti();

        // Update Text and Color
        const activeColor = googleColors[index % googleColors.length];
        btn.innerText = facts[index];
        btn.style.backgroundColor = activeColor;
        btn.style.color = (activeColor === "#FBBC05") ? "#000" : "#fff";
        btn.style.borderColor = activeColor;

        // Animation
        btn.style.transform = "scale(1.1)";
        setTimeout(() => btn.style.transform = "scale(1)", 150);

        index = (index + 1) % facts.length;
    });

});