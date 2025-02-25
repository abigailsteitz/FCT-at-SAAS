// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("SnowWhiteResult").style.display = "none";
    document.getElementById("RapunzelResult").style.display = "none";
    document.getElementById("MoanaResult").style.display = "none";
}
function seeResult() {
    var SnowWhite = 0;
    var Rapunzel = 0;
    var Moana = 0;

    if (document.getElementById("Apple").checked) {
        SnowWhite += 1;
    } else if (document.getElementById("Pear").checked) {
        Rapunzel += 1;

    } else if (document.getElementById("Coconut").checked) {
        Moana += 1;
    }

    if (document.getElementById("Yellow").checked) {
        SnowWhite += 1;
    } else if (document.getElementById("Purple").checked) {
        Rapunzel += 1;

    } else if (document.getElementById("Blue").checked) {
        Moana += 1;
    }

    if (document.getElementById("All of them!").checked) {
        SnowWhite += 1;
    } else if (document.getElementById("Chameleons").checked) {
        Rapunzel += 1;

    } else if (document.getElementById("Pigs").checked) {
        Moana += 1;
    }

    if (document.getElementById("Coffin").checked) {
        SnowWhite += 1;
    } else if (document.getElementById("Tower").checked) {
        Rapunzel += 1;
    } else if (document.getElementById("Island").checked) {
        Moana += 1;
    }

    if (document.getElementById("Cleaning").checked) {
        SnowWhite += 1;
    } else if (document.getElementById("Climbing").checked) {
        Rapunzel += 1;
    } else if (document.getElementById("Swimming").checked) {
        Moana += 1;
    }

    
    resetResult();

    if (Math.max(SnowWhite, Rapunzel, Moana) === SnowWhite) {
        document.getElementById("SnowWhiteResult").style.display = "block";
    } else if (Math.max(SnowWhite, Rapunzel, Moana) === Rapunzel) {
        document.getElementById("RapunzelResult").style.display = "block";
    } else if (Math.max(SnowWhite, Rapunzel, Moana) === Moana) {
        document.getElementById("MoanaResult").style.display = "block";
    }
}
