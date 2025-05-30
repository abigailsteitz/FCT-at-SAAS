// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

/* Your JavaScript code goes here */
/* === File: script.js === */
document.addEventListener("DOMContentLoaded", () => {
    console.log("Welcome to Chill Beans Coffee! ☕ Your energy is our mission.");
  });

 document.addEventListener('DOMContentLoaded', function() {
  const btn = document.getElementById('themeSwitcher');
  const body = document.body;

  // Load theme from localStorage
  if (localStorage.getItem('theme') === 'dark') {
    body.classList.add('dark-theme');
    btn.textContent = 'Switch to Light Theme';
  } else {
    btn.textContent = 'Switch to Dark Theme';
  }

  btn.addEventListener('click', function() {
    body.classList.toggle('dark-theme');
    if (body.classList.contains('dark-theme')) {
      localStorage.setItem('theme', 'dark');
      btn.textContent = 'Switch to Light Theme';
    } else {
      localStorage.setItem('theme', 'light');
      btn.textContent = 'Switch to Dark Theme';
    }
  });
});

// Theme switcher code here (if you have it already)

document.addEventListener('DOMContentLoaded', function() {
  // Sassy feedback
  const sassStrength = document.getElementById('sass-strength');
  const sassTemp = document.getElementById('sass-temp');
  const sassCups = document.getElementById('sass-cups');
  const sassFlavor = document.getElementById('sass-flavor');
  const sassMilk = document.getElementById('sass-milk');
  const cupsSlider = document.getElementById('cups');
  const cupsValue = document.getElementById('cups-value');
  const flavorSelect = document.getElementById('flavor');
  const milkCheckbox = document.getElementById('milk');

  // Strength sass
  document.querySelectorAll('input[name="strength"]').forEach(el => {
    el.addEventListener('change', function() {
      if (this.value === 'strong') sassStrength.textContent = "Whoa, someone likes to live on the edge!";
      else if (this.value === 'medium') sassStrength.textContent = "Classic. Respect.";
      else sassStrength.textContent = "Mild? You must be here for the vibes.";
    });
  });

  // Temp sass
  document.querySelectorAll('input[name="temp"]').forEach(el => {
    el.addEventListener('change', function() {
      if (this.value === 'hot') sassTemp.textContent = "Hot like your takes!";
      else sassTemp.textContent = "Cool beans, literally.";
    });
  });

  // Cups slider sass
  cupsSlider.addEventListener('input', function() {
    cupsValue.textContent = this.value;
    if (this.value >= 8) sassCups.textContent = "Are you okay? That's a lot of coffee!";
    else if (this.value >= 5) sassCups.textContent = "You run on caffeine, don't you?";
    else if (this.value == 1) sassCups.textContent = "Just one? Lightweight!";
    else sassCups.textContent = "";
  });

  // Flavor sass
  flavorSelect.addEventListener('change', function() {
    if (this.value === 'none') sassFlavor.textContent = "A true purist!";
    else sassFlavor.textContent = `Mmm, ${this.value} is a sweet choice.`;
  });

  // Milk sass
  milkCheckbox.addEventListener('change', function() {
    sassMilk.textContent = this.checked ? "Creamy dreams!" : "Keeping it classic!";
  });

  // Quiz logic
  const quizForm = document.getElementById('quizForm');
  if (quizForm) {
    quizForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const strength = quizForm.elements['strength'].value;
      const temp = quizForm.elements['temp'].value;
      const cups = quizForm.elements['cups'].value;
      const flavor = quizForm.elements['flavor'].value;
      const milk = quizForm.elements['milk'].checked;
      let result = "";

      // Fun logic for coffee recommendation
      if (cups >= 8) {
        result = "You need an IV drip of espresso. But seriously, try a Nitro Cold Brew!";
      } else if (strength === "strong" && temp === "hot" && !milk) {
        result = "Espresso is your perfect match!";
      } else if (strength === "medium" && temp === "hot" && milk) {
        result = "A classic Latte suits you best!";
      } else if (strength === "mild" && temp === "hot" && milk) {
        result = "Try a Flat White for a smooth experience!";
      } else if (temp === "cold" && milk) {
        result = "Iced Latte is your go-to!";
      } else if (temp === "cold" && !milk) {
        result = "Cold Brew is the way to go!";
      } else if (flavor === "mocha") {
        result = "Mocha for the win! Chocolate and coffee, best friends forever.";
      } else if (flavor === "hazelnut") {
        result = "Hazelnut Latte: You're a little nutty, and that's awesome.";
      } else if (flavor === "caramel") {
        result = "Caramel Macchiato: Sweet, smooth, and a little dramatic.";
      } else if (flavor === "vanilla") {
        result = "Vanilla Latte: Classic, but never boring.";
      } else {
        result = "A Cappuccino or Americano might be perfect for you!";
      }

      document.getElementById('quizResult').textContent = result;
      launchConfetti();
    });
  }

  // Confetti animation
  function launchConfetti() {
    const canvas = document.getElementById('confetti');
    canvas.style.display = 'block';
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    let pieces = [];
    for (let i = 0; i < 150; i++) {
      pieces.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height - canvas.height,
        r: Math.random() * 6 + 4,
        d: Math.random() * 50 + 10,
        color: `hsl(${Math.random()*360},70%,60%)`,
        tilt: Math.random() * 10 - 10
      });
    }
    let angle = 0;
    let frame = 0;
    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      angle += 0.01;
      for (let i = 0; i < pieces.length; i++) {
        let p = pieces[i];
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2, false);
        ctx.fillStyle = p.color;
        ctx.fill();
        p.y += Math.cos(angle + p.d) + 1 + p.r / 2;
        p.x += Math.sin(angle) * 2;
        if (p.y > canvas.height) {
          p.x = Math.random() * canvas.width;
          p.y = -10;
        }
      }
      frame++;
      if (frame < 120) {
        requestAnimationFrame(draw);
      } else {
        canvas.style.display = 'none';
      }
    }
    draw();
  }
});

