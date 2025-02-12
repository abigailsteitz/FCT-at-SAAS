// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("SillyResult").style.display = "none";
    document.getElementById("TacoResult").style.display = "none";
    document.getElementById("BaldResult").style.display = "none";
    document.getElementById("MustasheResult").style.display = "none";
}
function seeResult() {
    var SillyBron = 0;
    var TacoBron = 0;
    var BaldBron = 0;
    var MustasheBron = 0;


    if (document.getElementById("Taco").checked) {
        TacoBron += 1;
        MustasheBron +=1;
    } else if (document.getElementById("Egg").checked) {
        BaldBron += 1;
        
    } else {
        // Everything
        SillyBron += 1;
    }

    if (document.getElementById("TacoTuesday").checked) {
        MustasheBron += 1;
        TacoBron += 1;
    } else if (document.getElementById("BoomBoomBoomBoom").checked) {
        BaldBron += 1;
    } else {
        // ThatOurBallAintIt
        SillyBron += 1;
    }

    if (document.getElementById("Yes").checked) {
        SillyBron += 1;
        TacoBron += 1;
        BaldBron +=1;
    } else if (document.getElementById("No").checked) {
        MustasheBron += 1;
    }

    if (document.getElementById("Cavs").checked) {
        MustasheBron += 1;
    } else if (document.getElementById("Lakers").checked) {
        BaldBron += 1;
    } else if (document.getElementById("Heat").checked) {
        TacoBron += 1;
    } else {
        // All of them
        SillyBron += 1;
    }

    if (document.getElementById("LilBaby").checked) {
        BaldBron += 1;
    } else if (document.getElementById("TeeGrizzly").checked) {
        TacoBron += 1;
    } else if (document.getElementById("PopSmoke").checked) {
        SillyBron += 1;
    } else {
        // Other
        MustasheBron += 1;
    }

    resetResult();

    if (Math.max(BaldBron, SillyBron, MustasheBron, TacoBron) === BaldBron) {
        document.getElementById("BaldResult").style.display = "block";
    } else if (Math.max(BaldBron, SillyBron, MustasheBron, TacoBron) === SillyBron) {
        document.getElementById("SillyResult").style.display = "block";
    } else if (Math.max(BaldBron, SillyBron, MustasheBron, TacoBron) === MustasheBron) {
        document.getElementById("MustasheResult").style.display = "block";
    } else if (Math.max(BaldBron, SillyBron, MustasheBron, TacoBron) === TacoBron) {
        document.getElementById("TacoResult").style.display = "block";
    }
}
