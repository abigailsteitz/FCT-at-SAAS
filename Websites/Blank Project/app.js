// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

/* Your JavaScript code goes here */
// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("winterresult").style.display = "none";
    document.getElementById("springresult").style.display = "none";
    document.getElementById("fallresult").style.display = "none";
    document.getElementById("summerresult").style.display = "none";
}
function seeResult() {
    var summerscore = 0;
    var PlanktonScore = 0;
    var springscore = 0;
    var fallscore = 0;
    var winterscore = 0;

    if (document.getElementById("hot chocolate").checked) {
        winterscore += 1;
    } else if (document.getElementById("pumpkin spice").checked) {
        fallscore += 1;
        summerscore += 1;
        springscore += 1;
    } else {
        // 1, 2, 3 or more depending on the species
        PlanktonScore += 1;
    }

    if (document.getElementById("iced tea").checked) {
        fallscore += 1;
        winterscore += 1;
        springscore += 1;
    }
   
    

    if (document.getElementById("christmas").checked) {
        fallscore += 1;
        winterscore += 1;
    } else if (document.getElementById("4th of july").checked) {
        summerscore += 1;
        PlanktonScore += 1;
        springscore += 1;
    } else {
        // Use Diplomacy
        fallscore += 1;
    }

    if (document.getElementById("cold").checked) {
        winterscore += 1;
    } else if (document.getElementById("hot").checked) {
        summerscore += 1;
        PlanktonScore += 1;
    }

    if (document.getElementById("skiing").checked) {
        winterscore += 1;
    } else if (document.getElementById("beach trip").checked) {
        summerscore += 1;
    }
     else {
        // Existential Crisis
        fallscore += 1;
    }

    resetResult();

    var HighestScore = Math.max(summerscore, PlanktonScore, fallscore, winterscore, springscore);
    if (HighestScore === summerscore) {
        document.getElementById("winterresult").style.display = "block";
    } else if (HighestScore === PlanktonScore) {
        document.getElementById("springresult").style.display = "block";
    } else if (HighestScore === fallscore) {
        document.getElementById("fallresult").style.display = "block";
    } else if (HighestScore === winterscore) {
        document.getElementById("summerresult").style.display = "block";
    } else if (HighestScore === springscore) {
        document.getElementById("NudibranchResult").style.display = "block";
    }
}

