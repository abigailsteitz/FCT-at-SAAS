// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("BaddieResult").style.display = "none";
    document.getElementById("ChuzzResult").style.display = "none";
    document.getElementById("SillyResult").style.display = "none";
    document.getElementById("NiceResult").style.display = "none";
    document.getElementById("SadResult").style.display = "none";
}
function seeResult() {
    var Baddie = 0;
    var Chuzz = 0;
    var Silly = 0;
    var Nice = 0;
    var Sad = 0;
    var Angry =0;

    if (document.getElementById("8Eyes").checked) {
        Nice += 1;
    } else if (document.getElementById("2Eyes").checked) {
        Chuzz += 1;
        Silly += 1;
        Sad += 1;
    } else {
        // PlanktonEyes
        Baddie += 1;
        Angry += 1;
    }

    if (document.getElementById("Walk").checked) {
        Nice += 1;
        Chuzz += 1;
        Baddie += 1;
    } else if (document.getElementById("Swim").checked) {
        Sad += 1;
        Angry += 1;
        Baddie += 1;
    } else {
        // Swim upside down
        Chuzz += 1;
    }

    if (document.getElementById("Yes").checked) {
        Baddie += 1;
        Angry += 1;
    } else if (document.getElementById("No").checked) {
        Nice += 1;
        Sad += 1;
        Chuzz += 1;
    }

    if (document.getElementById("Fight").checked) {
        Baddie += 1;
    } else if (document.getElementById("Run").checked) {
        Chuzz += 1;
        Sad += 1;
    } else if (document.getElementById("Secrete").checked) {
        Nice += 1;
    } else {
        // Use Diplomacy
        Angry += 1;
    }

    if (document.getElementById("Of course").checked) {
        Baddie += 1;
    } else if (document.getElementById("Probably not").checked) {
        Angry += 1;
    } else if (document.getElementById("Head empty").checked) {
        Nice += 1;
        Sad += 1;
    } else {
        // Existential Crisis
        Chuzz += 1;
    }

    resetResult();

    if (Math.max(Baddie, Angry, Sad, Chuzz, Nice) === Baddie) {
        document.getElementById("BaddieResult").style.display = "block";
    } else if (Math.max(Baddie, Angry, Sad, Chuzz, Nice) === Angry) {
        document.getElementById("AngryResult").style.display = "block";
    } else if (Math.max(Baddie, Angry, Sad, Chuzz, Nice) === Sad) {
        document.getElementById("SadResult").style.display = "block";
    } else if (Math.max(Baddie, Angry, Sad, Chuzz, Nice) === Chuzz) {
        document.getElementById("ChuzzResult").style.display = "block";
    } else if (Math.max(Baddie, Angry, Sad, Chuzz, Nice) === Nice) {
        document.getElementById("NiceResult").style.display = "block";
    }
}
