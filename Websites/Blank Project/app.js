<script>
'use strict';

function resetResult() {
  document.getElementById("GenZResult").style.display = "none";
  document.getElementById("GenAlphaResult").style.display = "none";
  document.getElementById("errorMessage").style.display = "none";
}

function allAnswered() {
  const groups = ["show", "app", "freeTime", "slang", "style"];
  for (let group of groups) {
    const options = document.getElementsByName(group);
    let oneChecked = false;
    for (let option of options) {
      if (option.checked) {
        oneChecked = true;
        break;
      }
    }
    if (!oneChecked) return false;
  }
  return true;
}

function seeResult() {
  resetResult();

  if (!allAnswered()) {
    document.getElementById("errorMessage").style.display = "block";
    return;
  }

  let genZScore = 0;
  let genAlphaScore = 0;

  // Scoring
  if (document.getElementById("iCarly").checked) genZScore++;
  if (document.getElementById("PeppaPig").checked) genZScore++;
  if (document.getElementById("Cocomelon").checked) genAlphaScore++;

  if (document.getElementById("Instagram").checked) genZScore++;
  if (document.getElementById("TikTok").checked) {
    genZScore++;
    genAlphaScore++;
  }
  if (document.getElementById("Roblox").checked) genAlphaScore++;

  if (document.getElementById("Scroll").checked) genZScore++;
  if (document.getElementById("Gaming").checked) genAlphaScore++;
  if (document.getElementById("MakeEdits").checked) genAlphaScore++;

  if (document.getElementById("Slay").checked) genZScore++;
  if (document.getElementById("Rizz").checked) genAlphaScore++;
  if (document.getElementById("Bet").checked) genZScore++;

  if (document.getElementById("Y2K").checked) genZScore++;
  if (document.getElementById("Oversized").checked) genAlphaScore++;
  if (document.getElementById("CozyCore").checked) genAlphaScore++;

  // Show result
  if (genZScore >= genAlphaScore) {
    document.getElementById("GenZResult").style.display = "block";
  } else {
    document.getElementById("GenAlphaResult").style.display = "block";
  }
}
</script>
</body>
</html>
