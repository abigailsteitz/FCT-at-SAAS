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