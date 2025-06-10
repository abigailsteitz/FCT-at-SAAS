// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("AppleResult").style.display = "none";
    document.getElementById("MangoResult").style.display = "none";
    document.getElementById("StrawberryResult").style.display = "none";
    document.getElementById("GrapeResult").style.display = "none";
}
function seeResult() {
    var AppleScore = 0;
    var MangoScore = 0;
    var StrawberryScore = 0;
    var GrapeScore = 0;

    if (document.getElementById("Red").checked) {
        AppleScore += 1;
    } else if (document.getElementById("Green").checked) {
        MangoScore += 1;
        StrawberryScore += 1;
        GrapeScore += 1;
    }

    if (document.getElementById("Walk").checked) {
        AppleScore += 1;
        MangoScore += 1;
        StrawberryScore += 1;
    } else if (document.getElementById("Swim").checked) {
        StrawberryScore += 1;
        GrapeScore += 1;
    }
    if (document.getElementById("Yes").checked) {
        AppleScore += 1;
        MangoScore += 1;
    } else if (document.getElementById("No").checked) {
        StrawberryScore += 1;
        GrapeScore += 1;
    }

    if (document.getElementById("Fight").checked) {
        MangoScore += 1;
    } else if (document.getElementById("Run").checked) {
        StrawberryScore += 1;
        GrapeScore += 1;
    } else if (document.getElementById("Secrete").checked) {
        GrapeScore += 1;
    } else {
        // Use Diplomacy
        AppleScore += 1;
    }

    if (document.getElementById("Of course").checked) {
        MangoScore += 1;
    } else if (document.getElementById("Probably not").checked) {
        StrawberryScore += 1;
    } else if (document.getElementById("Head empty").checked) {
        GrapeScore += 1;
        AppleScore += 1;
    } else {
        // Existential Crisis
        HumanScore += 1;
    }

    resetResult();

    var HighestScore = Math.max(AppleScore, MangoScore, StrawberryScore, GrapeScore);
    if (HighestScore === AppleScore) {
        document.getElementById("AppleResult").style.display = "block";
    } else if (HighestScore === MangoScore) {
        document.getElementById("MangoResult").style.display = "block";
    } else if (HighestScore === StrawberryScore) {
        document.getElementById("StrawberryResult").style.display = "block";
    } else if (HighestScore === GrapeScore) {
        document.getElementById("GrapeResult").style.display = "block";
    }
}
