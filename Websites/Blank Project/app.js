// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';


function resetResult() {
    document.getElementById("Royalblue").style.display = "none";
    document.getElementById("lightpink").style.display = "none";
    document.getElementById("babyblue").style.display = "none";
    document.getElementById("paleyellow").style.display = "none";
    document.getElementById("BlackDarkgrey").style.display = "none";
}
function seeResult() {
    var RoyalblueScore = 0;
    var lightpinkScore = 0;
    var babyblueScore = 0;
    var paleyellowScore = 0;
    var BlackDarkgreyScore = 0;

    if (document.getElementById("Fall").checked) {
        paleyellowScore += 1;
        BlackDarkgreyScore += 1;
    } 
    if (document.getElementById("Winter").checked) {
        RoyalblueScore += 1;
        BlackDarkgreyScore += 1;
    } if (document.getElementById("Spring").checked) {
        lightpinkScore += 1;
    }
if (document.getElementById("Summer").checked) {
        lightpinkScore += 1;
        babyblueScore += 1;
        paleyellowScore += 1;
        }
    if (document.getElementById("Warm").checked) {
        lightpinkScore += 1;
        paleyellowScore += 1;
    }
    if (document.getElementById("Cool").checked) {
        RoyalblueScore += 1;
        babyblueScore += 1;
        BlackDarkgreyScore += 1;
    }


    if (document.getElementById("Red").checked) {
        lightpinkScore += 1;
        BlackDarkgreyScore += 1;
    } if (document.getElementById("Orange").checked) {
        lightpinkScore += 1;
        paleyellowScore += 1;
    } if (document.getElementById("Yellow").checked) {
        paleyellowScore += 1;  
    } if (document.getElementById("Green").checked) {
        BlackDarkgreyScore += 1;
    } if (document.getElementById("Blue").checked) {
        RoyalblueScore += 1;
        babyblueScore += 1;
    } if (document.getElementById("Indigo").checked) {

        babyblueScore += 1;
    } if (document.getElementById("black").checked) {
        BlackDarkgreyScore += 1;
    } if (document.getElementById("Turquoise").checked) {

        babyblueScore += 1;

 } if (document.getElementById("Brunette").checked) {
        babyblueScore += 1;
        paleyellowScore += 1;
        BlackDarkgreyScore += 1;
 } if (document.getElementById("Blonde").checked) {
        lightpinkScore += 1;
        paleyellowScore += 1;
 } if (document.getElementById("Black").checked) {
        RoyalblueScore += 1;
        BlackDarkgreyScore += 1;
        babyblueScore += 1;
 } if (document.getElementById("Pink").checked) {
        lightpinkScore += 1;
        paleyellowScore += 1;
 } if (document.getElementById("Blue").checked) {
        RoyalblueScore += 1;
        babyblueScore += 1;

    
} if (document.getElementById("Cleangirl").checked) {
        lightpinkScore += 1;
        paleyellowScore += 1;
 } if (document.getElementById("Emo").checked) {
        BlackDarkgreyScore += 1;
 } if (document.getElementById("Preppy").checked) {
        lightpinkScore += 1;
        paleyellowScore += 1;
        lightblueScore += 1;
 } if (document.getElementById("Skater").checked) {
        RoyalblueScore += 1;
        BlackDarkgreyScore += 1;
 }
    resetResult();


    var HighestScore = Math.max(RoyalblueScore, lightpinkScore, babyblueScore, paleyellowScore, BlackDarkgreyScore); 
    if (HighestScore === RoyalblueScore) {
        document.getElementById("RoyalblueResult").style.display = "block";
    } 
    else if (HighestScore === lightpinkScore) {
        document.getElementById("lightpinkResult").style.display = "block";
    } 
    else if (HighestScore === babyblueScore) {
        document.getElementById("babyblueResult").style.display = "block";
    } else if (HighestScore === paleyellowScore) {
        document.getElementById("paleyellowResult").style.display = "block";
    } else if (HighestScore === BlackDarkgreyScore) {
        document.getElementById("BlackDarkgreyResult").style.display = "block";
    }
}


