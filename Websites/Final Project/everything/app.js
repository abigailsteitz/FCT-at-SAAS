'use strict';

document.addEventListener('DOMContentLoaded', function() {
  // Highlight the current page in navigation
  const links = document.querySelectorAll('nav a');
  links.forEach(link => {
    if (link.href === window.location.href) {
      link.style.fontWeight = 'bold';
      link.style.textDecoration = 'underline';
    }
    });
  });

  // Make all images responsive
  const images = document.querySelectorAll('img');
  images.forEach(img => {
    img.style.maxWidth = '300px';
    img.style.height = 'auto';
    img.style.display = 'block';
    img.style.margin = '1em auto';
  });


  // Smooth scroll to top button (if you add a button with id="to-top")
  const toTopBtn = document.getElementById('to-top');
  if (toTopBtn) {
    toTopBtn.addEventListener('click', function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Personality quiz logic (quiz.html)
const quizForm = document.getElementById('personality-quiz');
if (quizForm) {
  quizForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting and refreshing

    let conservativeScore = 0;
    let liberalScore = 0;
    let moderateScore = 0;

    // Get all question names
    const questions = ["taxes", "healthcare", "climate", "guns", "values", "abortion", "immigration"];

    questions.forEach(q => {
      const selected = document.querySelector(`input[name="${q}"]:checked`);
      if (selected) {
        if (selected.value === "conservative") {
          conservativeScore++;
        } else if (selected.value === "liberal") {
          liberalScore++;
        } else if (selected.value === "moderate") {
          moderateScore++;
        }
      }
    });

    // Determine the result
    let resultText = "";
    if (conservativeScore > liberalScore && conservativeScore > moderateScore) {
      resultText = "You lean Republican. God, guns, opressing the minoritys, and tax cuts for the rich. well arnt u a caring person.";
    } else if (liberalScore > conservativeScore && liberalScore > moderateScore) {
      resultText = "You lean Democrat. Hope, progress, and vision for a better future.";
    } else if (moderateScore >= conservativeScore && moderateScore >= liberalScore) {
      resultText = "You’re a Centrist. Fence-sitter, peacemaker, or chaos agent? Depends who you ask.";
    } else {
      resultText = "Your results are mixed. Maybe you just like arguing.";
    }

    // Show result
    const resultDiv = document.getElementById("quiz-result");
    resultDiv.style.display = "block";
    resultDiv.textContent = resultText;
  });
}