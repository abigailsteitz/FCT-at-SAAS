// Slideshow logic
const images = [
    "https://i0.wp.com/stewartlighting.com/wp-content/uploads/2022/02/shutterstock_1483369076.jpg?fit=1000%2C667&ssl=1",
    "https://i.pinimg.com/736x/81/cd/bb/81cdbb810a24359e2e2806cbe8ebb57c.jpg",
    "https://www.thespruce.com/thmb/5yz1IGN5zBsRDsCWzl7NSEzxEK8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/loafhome-e56f050c9e43484cbe190ce3ab1ca3d3.jpg",
    "https://www.bhg.com/thmb/jaD28JajtQv9FoMAnbHWyM0UGFw=/4000x0/filters:no_upscale():strip_icc()/Livingroom-Capture-One-Session13717-CiF-_0XRK7VA0sclpsCm2P-27fbe3d5f41d4cb49d047e345db4d00a.jpg"
];
let current = 0;
function showSlide(idx) {
    const img = document.getElementById('slideshow-img');
    current = (idx + images.length) % images.length;
    img.src = images[current];
}
function prevSlide() {
    showSlide(current - 1);
}
function nextSlide() {
    showSlide(current + 1);
}

// Touch swipe support for slideshow
document.addEventListener('DOMContentLoaded', function() {
    const img = document.getElementById('slideshow-img');
    if (img) {
        let startX = 0;
        let endX = 0;
        img.addEventListener('touchstart', function(e) {
            if (e.touches.length === 1) {
                startX = e.touches[0].clientX;
            }
        });
        img.addEventListener('touchmove', function(e) {
            if (e.touches.length === 1) {
                endX = e.touches[0].clientX;
            }
        });
        img.addEventListener('touchend', function() {
            const diff = endX - startX;
            if (Math.abs(diff) > 40) {
                if (diff < 0) {
                    nextSlide();
                } else {
                    prevSlide();
                }
            }
            startX = 0;
            endX = 0;
        });
    }
});

// Parallax scroll effect for image strip (if present)
window.addEventListener('scroll', function() {
    const parallax = document.getElementById('parallaxImages');
    if (parallax) {
        parallax.style.transform = `translateX(${-window.scrollY * 2}px)`;
    }
});

// Parallax scroll effect for vertical side images
window.addEventListener('scroll', function() {
    const scrollY = window.scrollY;
    const left = document.getElementById('parallaxLeft');
    const right = document.getElementById('parallaxRight');
    if (left) left.style.transform = `translateY(${-scrollY * 2}px)`;
    if (right) right.style.transform = `translateY(${-scrollY * 2}px)`;
});

// Theme persistence across pages
function applyTheme() {
    if (localStorage.getItem('theme') === 'dusty-blue') {
        document.body.classList.add('dusty-blue');
    } else {
        document.body.classList.remove('dusty-blue');
    }
}
function toggleTheme() {
    if (document.body.classList.contains('dusty-blue')) {
        document.body.classList.remove('dusty-blue');
        localStorage.setItem('theme', 'default');
    } else {
        document.body.classList.add('dusty-blue');
        localStorage.setItem('theme', 'dusty-blue');
    }
}
document.addEventListener('DOMContentLoaded', applyTheme);

// Spin wheel modal logic
let spinning = false;
function closeSpinModal() {
    if (spinning) return;
    document.getElementById('spinWheelModal').style.display = 'none';
    document.getElementById('spinWheel').style.transform = 'rotate(0deg)';
}
function spinSVGWheel() {
    if (spinning) return;
    spinning = true;
    const wheel = document.getElementById('spinWheel');
    // Ensure at least 720 degrees (2 full spins)
    const minSpins = 2;
    const minDegrees = 360 * minSpins;
    const extra = Math.floor(Math.random() * 360);
    const totalRotation = minDegrees + (360 * 3) + extra; // 5+ spins as before, but always at least 720deg
    wheel.style.transform = `rotate(${totalRotation}deg)`;
    const degree = (360 - (extra % 360)) % 360;
    const index = Math.floor(degree / 60);
    const prizes = [
        "50% OFF",
        "Buy One Get One",
        "$25 Gift Card",
        "10% OFF",
        "Mystery Gift",
        "Try Again"
    ];
    setTimeout(() => {
        alert("🎉 You won: " + prizes[index]);
        spinning = false;
    }, 4000);
}

// Expose functions to global scope for inline HTML event handlers
window.prevSlide = prevSlide;
window.nextSlide = nextSlide;
window.toggleTheme = toggleTheme;
window.closeSpinModal = closeSpinModal;
window.spinSVGWheel = spinSVGWheel;

// If you have a language switcher function, expose it as well
if (typeof toggleLanguage === "function") {
    window.toggleLanguage = toggleLanguage;
}
