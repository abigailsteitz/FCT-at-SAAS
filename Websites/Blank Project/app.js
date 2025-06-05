// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';


function resetResult() {
    document.getElementById("RingResult").style.display = "none";
    document.getElementById("NecklaceResult").style.display = "none";
    document.getElementById("BraceletResult").style.display = "none";
}
function seeResult() {
    var RingScore = 0;
    var NecklaceScore = 0;
    var BraceletScore = 0;
 

    if (document.getElementById("pink").checked) {
        BraceletScore += 1;
    }
    if (document.getElementById("gold").checked) {
        RingScore += 1;
        BraceletScore += 1;
        NecklaceScore += 1;
    
    } else if (document.getElementById("silver").checked) {
        NecklaceScore += 1;
    }

    if (document.getElementById("ring").checked) {
        RingScore += 1;
    }
    if (document.getElementById("necklace").checked) {
        NecklaceScore += 1;
    }
    if (document.getElementById("bracelet").checked) {
        BraceletScore += 1;
    }

    if (document.getElementById("swirl").checked) {
        RingScore += 1;
    }
    if (document.getElementById("hearts").checked) {
        BraceletScore += 1;
    }
    if (document.getElementById("stars").checked) {
        NecklaceScore += 1;
    }

    resetResult();


    var HighestScore = Math.max(RingScore, NecklaceScore, BraceletScore);
    if (HighestScore === RingScore) {
        document.getElementById("RingResult").style.display = "block";
    }
    if (HighestScore === NecklaceScore) {
        document.getElementById("NecklaceResult").style.display = "block";
    }
    if (HighestScore === BraceletScore) {
        document.getElementById("BraceletResult").style.display = "block";
    }
    if (HighestScore === 0) {
        document.getElementById("Their All good for you! go with your gut!").style.display = "block";
    }
}