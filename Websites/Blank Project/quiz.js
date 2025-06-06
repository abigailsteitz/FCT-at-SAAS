'use strict';


function resetResult() {
    document.getElementById("wingerResult").style.display = "none";
    document.getElementById("strikerResult").style.display = "none";
    document.getElementById("goalieResult").style.display = "none";
}
function seeResult() {
    var wingerScore = 0;
    var strikerScore = 0;
    var goalieScore = 0;


    if (document.getElementById("yes").checked) {
        wingerScore += 1;
        strikerScore += 1;

    } else {
        // 1, 2, 3 or more depending on the species
        goalieScore+= 1;
    }

if (document.getElementById("yes").checked) {
        goalieScore += 1;
        strikerScore += 1;

    } else {
        // 1, 2, 3 or more depending on the species
        wingerScore+= 1;
    }

if (document.getElementById("yes").checked) {
        wingerScore += 1;
        strikerScore += 1;

    } else {
        // 1, 2, 3 or more depending on the species
        goalieScore+= 1;
    }

if (document.getElementById("yes").checked) {
        wingerScore += 1;
        strikerScore += 1;

    } else {
        // 1, 2, 3 or more depending on the species
        goalieScore+= 1;
    }

if (document.getElementById("yes").checked) {
        goalieScore += 1;

    } else {
        // 1, 2, 3 or more depending on the species
        wingerScore+= 1;
        strikerScore += 1;
    }




    resetResult();


    var HighestScore = Math.max(wingerScore, strikerScore, goalieScore);
    if (HighestScore === wingerScore) {
        document.getElementById("wingerResult").style.display = "block";
    } else if (HighestScore === goalieScore) {
        document.getElementById("goalieResult").style.display = "block";
    } else if (HighestScore === strikerScore) {
        document.getElementById("strikerResult").style.display = "block";
    }
}
