// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("RedResult").style.display = "none";
    document.getElementById("YellowResult").style.display = "none";
    document.getElementById("GreenResult").style.display = "none";
    document.getElementById("BlueResult").style.display = "none";
    document.getElementById("PinkResult").style.display = "none";
}
function seeResult() {
    var Red = 0;
    var Yellow = 0;
    var Green = 0;
    var Blue = 0;
    var Pink = 0;

    if (document.getElementById("annoyed").checked) {
        Red += 1;
    } else if (document.getElementById("calm").checked) {
        Green += 1;
        Blue += 1;
        
    } else {
        // happy
        Yellow += 1;
        Pink += 1;

    }

    if (document.getElementById("Fire").checked) {
        Red += 1;
        Pink += 1;
        
    } else if (document.getElementById("Water").checked) {
        Blue += 1;
        
    } else {
        // Light
        Yellow += 1;
    }

    if (document.getElementById("Warm").checked) {
        Red += 1;
        Yellow += 1;
        Pink += 1;
    } else if (document.getElementById("Cool").checked) {
        Green += 1;
        Blue += 1;
        
    }

    if (document.getElementById("Fight").checked) {
        Red += 1;
    } else if (document.getElementById("Run").checked) {
        Yellow += 1;
        Pink += 1;
    }  else {
        // Use Diplomacy
        Green += 1;
        Blue += 1;
    }

    if (document.getElementById("Chill").checked) {
        Green += 1;
        Blue += 1;
    } else if (document.getElementById("Bubbly").checked) {
        Pink += 1;
    } else if (document.getElementById("Confrontational").checked) {
        Red += 1;
        
    } else {
        // A ray of sunshine
        Yellow += 1;
    }

    resetResult();

    if (Math.max(Red, Yellow, Green, Blue, Pink) === Red) {
        document.getElementById("RedResult").style.display = "block";
    } else if (Math.max(Red, Yellow, Green, Blue, Pink) === Yellow) {
        document.getElementById("YellowResult").style.display = "block";
    } else if (Math.max(Red, Yellow, Green, Blue, Pink) === Green) {
        document.getElementById("GreenResult").style.display = "block";
    } else if (Math.max(Red, Yellow, Green, Blue, Pink) === Blue) {
        document.getElementById("BlueResult").style.display = "block";
    } else if (Math.max(Red, Yellow, Green, Blue, Pink) === Pink) {
        document.getElementById("PinkResult").style.display = "block";
    }
}

