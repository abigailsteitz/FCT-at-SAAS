window.onload = function() {
  document.getElementById('petQuiz').onclick = function(event) {
    event.preventDefault();
    let score = 0;
    const form = event.target;
    if(form.q1.value === "yes") score++;
    if(form.q2.value === "yes") score++;
    if(form.q3.value === "no") score++;
    if(form.q4.value === "no") score++;
    if(form.q5.value === "yes") score++;

    let resultDiv = document.getElementById('quizResult');
    if(score >= 4) {
      resultDiv.innerHTML = 'You should adopt a Tibetan Mastiff! <a href="tibetanmastiff.html">Click here for more information</a>';
    } else if(score >= 2) {
      resultDiv.innerHTML = 'You should adopt a Victoria Crowned Pigeon! <a href="victoriacrownedpidgeon.html">Click here for more information</a>';
    } else {
      resultDiv.innerHTML = 'You should adopt a Chameleon! <a href="chameleon.html">Click here for more information</a>';
    }
    document.getElementById('revealBtn').style.display = 'none';
  }
};