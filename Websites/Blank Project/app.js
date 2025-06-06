/* Your JavaScript code goes here */
// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("SaturnResult").style.display = "none";
    document.getElementById("NeptuneResult").style.display = "none";
    document.getElementById("StayResult").style.display = "none";
}

function seeResult() {
    var SaturnScore = 0;
    var NeptuneScore = 0;
    var StayScore = 0;

    if (document.getElementById("YesSnow").checked) {
        SaturnScore += 1;
    } else if (document.getElementById("MaybeSnow").checked) {
        NeptuneScore += 1;
    } else {
        StayScore += 1;
    }

    if (document.getElementById("YesRings").checked) {
        StayScore += 1;
        NeptuneScore += 1;
    } else if (document.getElementById("EarRings").checked) {
        SaturnScore += 1;
    }

    if (document.getElementById("Hot").checked) {
        SaturnScore += 1;
        StayScore += 1;
    } else {
        NeptuneScore += 1;
    }

    resetResult();

    var HighestScore = Math.max(SaturnScore, NeptuneScore, StayScore);
    if (HighestScore === SaturnScore) {
        document.getElementById("SaturnResult").style.display = "block";
    } else if (HighestScore === NeptuneScore) {
        document.getElementById("NeptuneResult").style.display = "block";
    } else if (HighestScore === StayScore) {
        document.getElementById("StayResult").style.display = "block";
    }
}
