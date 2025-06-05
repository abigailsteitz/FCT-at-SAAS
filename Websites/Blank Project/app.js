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
    } 
    if (document.getElementById("silver").checked) {
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

    if (document.getElementById("eyes").checked) {
        NecklaceScore += 1;
    }
    if (document.getElementById("nails").checked) {
        BraceletScore += 1;
        RingScore += 1;
    }
    if (document.getElementById("mornings").checked) {
        BraceletScore += 1;
    }
    if (document.getElementById("evenings").checked) {
        NecklaceScore += 1;
    }
    if (document.getElementById("neither").checked) {
        RingScore += 1;
    }
    
    resetResult();


    var HighestScore = Math.max(RingScore, NecklaceScore, BraceletScore);
     if (HighestScore === RingScore && HighestScore === NecklaceScore && HighestScore === BraceletScore) {
        document.getElementById("AllResult").style.display = "block";
    }
    else if (HighestScore === RingScore) {
        document.getElementById("RingResult").style.display = "block";
    }
    else if (HighestScore === NecklaceScore) {
        document.getElementById("NecklaceResult").style.display = "block";
    }
    else if (HighestScore === BraceletScore) {
        document.getElementById("BraceletResult").style.display = "block";
    }
}