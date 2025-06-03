document.getElementById('quizForm').addEventListener('submit', function (event) {
  event.preventDefault();

  const answers = ['q1', 'q2', 'q3', 'q4', 'q5'].map(q => {
    const selected = document.querySelector(`input[name="${q}"]:checked`);
    return selected ? selected.value : null;
  });

  if (answers.includes(null)) {
    document.getElementById('result').innerHTML = "<p>Please answer all questions.</p>";
    return;
  }

  const counts = { shark: 0, puffer: 0, sailfish: 0 };
  answers.forEach(answer => counts[answer]++);

  const result = Object.entries(counts).reduce((a, b) => b[1] > a[1] ? b : a)[0];

  let message = "", image = "", alt = "", link = "";

  if (result === "shark") {
    message = `<h2>You got <span class="highlight">Sammy the Shark!</span></h2><p>You’re bold, adventurous, and always on the move!</p>`;
    image = "https://sharksandrays.com/wp-content/uploads/2020/09/Blacktip-Reef-Shark-011.jpg";
    alt = "Sammy the Shark";
    link = "fishtank.html#sammy";
  } else if (result === "puffer") {
    message = `<h2>You got <span class="highlight">Puffy the Pufferfish!</span></h2><p>You’re chill, creative, and full of surprises!</p>`;
    image = "https://i.natgeofe.com/k/b7a6ee44-f96f-434a-8606-6ae742f6ab23/pufferfish-inflated-closeup_square.jpg";
    alt = "Puffy the Pufferfish";
    link = "fishtank.html#puffy";
  } else if (result === "sailfish") {
    message = `<h2>You got <span class="highlight">Sally the Sailfish!</span></h2><p>You’re graceful, stylish, and full of flair!</p>`;
    image = "https://cdn.britannica.com/46/9546-050-42565668/sailfish-Indo-Pacific.jpg?w=300";
    alt = "Sally the Sailfish";
    link = "fishtank.html#sally";
  }

  document.getElementById('result').innerHTML = `
    <div class="result-card fade-in">
      ${message}
      <a href="${link}">
        <img src="${image}" alt="${alt}" class="result-img" title="Click to learn more about ${alt}">
      </a>
      <p><em>Click the image to meet your FinFriend!</em></p>
    </div>
  `;

  launchConfetti();
});

// Confetti 🎉
function launchConfetti() {
  const script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js';
  script.onload = () => {
    const duration = 2 * 1000;
    const end = Date.now() + duration;

    (function frame() {
      confetti({
        particleCount: 5,
        angle: 60,
        spread: 55,
        origin: { x: 0 }
      });
      confetti({
        particleCount: 5,
        angle: 120,
        spread: 55,
        origin: { x: 1 }
      });

      if (Date.now() < end) {
        requestAnimationFrame(frame);
      }
    })();
  };
  document.body.appendChild(script);
}
