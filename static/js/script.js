// Responsive Navbar Toggle
function toggleMobileMenu() {
    const mobileMenu = document.getElementById('mobileMenu');
    mobileMenu.classList.toggle('hidden');
}

// Form Validation
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const contactForm = document.getElementById('contactForm');

    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Basic validation
            if (username && password) {
                // Simulate login (replace with actual authentication)
                alert('Login successful!');
                window.location.href = 'validate.html';
            } else {
                alert('Please enter username and password');
            }
        });
    }

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // Simulate contact form submission
            alert('Message sent successfully!');
            e.target.reset();
        });
    }
});

// Responsive Design Utilities
function handleResponsiveDesign() {
    const screenWidth = window.innerWidth;
    const navLinks = document.querySelector('.nav-links');
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');

    if (screenWidth <= 768) {
        // Mobile view
        if (navLinks) navLinks.classList.add('hidden');
        if (mobileMenuToggle) mobileMenuToggle.classList.remove('hidden');
    } else {
        // Desktop view
        if (navLinks) navLinks.classList.remove('hidden');
        if (mobileMenuToggle) mobileMenuToggle.classList.add('hidden');
    }
}

// Run on load and window resize
window.addEventListener('load', handleResponsiveDesign);
window.addEventListener('resize', handleResponsiveDesign);