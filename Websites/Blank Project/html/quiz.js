function getQuizResult() {
  let scores = { basic: 0, pro: 0, deluxe: 0 };
  // Questions 1-3 (radio)
  for (let i = 1; i <= 3; i++) {
    let answer = document.querySelector(`input[name="q${i}"]:checked`);
    if (answer) scores[answer.value]++;
  }
  // Question 4 (dropdown)
  let q4 = document.getElementById("q4");
  if (q4 && q4.value) scores[q4.value]++;

  // Bonus: If they pick both case and brush, push toward deluxe!
  let bonus = Array.from(document.querySelectorAll('input[name="bonus"]:checked')).map(cb => cb.value);
  if (bonus.includes("case") && bonus.includes("brush")) scores.deluxe++;
  else if (bonus.includes("brush")) scores.pro++;
  else if (bonus.includes("case")) scores.basic++;

  // Sassy feedback
  let sassy = [
    "Wow, you must REALLY love eating at your laptop.",
    "Your keyboard called. It wants a vacation.",
    "You sound like a cleaning pro!",
    "You deserve the best. Or at least, the cleanest."
  ];

  // Find the highest score
  let result;
  if (scores.deluxe >= scores.pro && scores.deluxe >= scores.basic) {
    result = `
      <h2>You need: KeyFix Deluxe!</h2>
      <img src="./images/keyfix-deluxe.jpg" alt="KeyFix Deluxe" style="max-width:300px;">
      <p>${sassy[Math.floor(Math.random()*sassy.length)]}</p>
      <p>Our most advanced tool, with all the bells and whistles. Your keyboard will thank you!</p>
    `;
  } else if (scores.pro >= scores.basic) {
    result = `
      <h2>You need: KeyFix Pro!</h2>
      <img src="./images/keyfix-pro.jpg" alt="KeyFix Pro" style="max-width:300px;">
      <p>${sassy[Math.floor(Math.random()*sassy.length)]}</p>
      <p>Perfect for gadget lovers and those who want a little extra cleaning power.</p>
    `;
  } else {
    result = `
      <h2>You need: KeyFix Basic!</h2>
      <img src="./images/keyfix-basic.jpg" alt="KeyFix Basic" style="max-width:300px;">
      <p>${sassy[Math.floor(Math.random()*sassy.length)]}</p>
      <p>Simple, effective, and gets the job done. Sometimes less is more!</p>
    `;
  }

  // Show result and confetti
  document.getElementById("quizResult").innerHTML = result;
  document.getElementById("quizResult").classList.remove("hidden");
  document.getElementById("confetti").classList.remove("hidden");

  // Simple celebratory animation
  let confetti = document.getElementById("confetti");
  confetti.style.fontSize = "2rem";
  confetti.style.transition = "all 0.5s";
  setTimeout(() => {
    confetti.style.fontSize = "4rem";
    setTimeout(() => {
      confetti.style.fontSize = "2rem";
    }, 800);
  }, 100);
}
