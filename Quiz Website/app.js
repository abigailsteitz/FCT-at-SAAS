// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("Stonecoldresult").style.display = "none";
    document.getElementById("SmokeResult").style.display = "none";
    document.getElementById("FadeResult").style.display = "none";
    document.getElementById("MatteResult").style.display = "none";
    document.getElementById("WineResult").style.display = "none";
}
function seeResult() {
    var Stonecoldfox = 0;
    var SmokeNroses = 0;
    var Fadeintohue = 0;
    var Matteabouthue = 0;
    var Wineonly = 0;

    if (document.getElementById("Fire").checked) {
        SmokeNroses += 1;
    } else if (document.getElementById("Earth").checked) {
        Stonecoldfox += 1;
        Matteabouthue += 1;
    } else if (document.getElementById("Water").checked) {
        Wineonly += 1;
    }
    else {
        Fadeintohue += 1;
    }

    if (document.getElementById("Introspective").checked) {
        Fadeintohue += 1;
    } else if (document.getElementById("Reliable").checked) {
        Stonecoldfox += 1;
    } else if (document.getElementById("Poised").checked) {
        Wineonly += 1;
    }else if (document.getElementById("Balanced").checked) {
        Matteabouthue += 1;
    }else if (document.getElementById("Artsy").checked) {
        SmokeNroses += 1;
    }else {
        Wineonly += 1;
    }

    if (document.getElementById("Coffee").checked) {
        SmokeNroses += 1;
    } else if (document.getElementById("Avacado").checked) {
        Wineonly += 1;
    }else if (document.getElementById("Oatmeal").checked) {
        Matteabouthue += 1;
    }else if (document.getElementById("Smoothie").checked) {
        Fadeintohue += 1;
    }else if (document.getElementById("Pancakes").checked) {
        Stonecoldfox += 1;
    }else {
        SmokeNroses += 1;
    }

    if (document.getElementById("Home").checked) {
        Matteabouthue += 1;
    } else if (document.getElementById("Friends").checked) {
        Wineonly += 1;
    } else if (document.getElementById("Mall").checked) {
        SmokeNroses += 1;
    } else if (document.getElementById("Movies").checked) {
        Fadeintohue += 1;
    } else if (document.getElementById("Hike").checked) {
        Stonecoldfox += 1;
    } else {
       Stonecoldfox += 1;
    }

    if (document.getElementById("OceanBreeze").checked) {
        Stonecoldfox += 1;
    } else if (document.getElementById("CashmereVanilla").checked) {
        Fadeintohue += 1;
    } else if (document.getElementById("LavenderChamomile").checked) {
        Wineonly += 1;
    } else if (document.getElementById("SandalwoodAmber").checked) {
        Matteabouthue += 1;
    } else if (document.getElementById("Tangerine").checked) {
        SmokeNroses += 1;
    } else {
        Matteabouthue += 1;
    }

    resetResult();

    if (Math.max(Matteabouthue, SmokeNroses, Wineonly, Fadeintohue, Stonecoldfox) === Matteabouthue) {
        document.getElementById("MatteResult").style.display = "block";
    } else if (Math.max(Matteabouthue, SmokeNroses, Wineonly, Fadeintohue, Stonecoldfox) === SmokeNroses) {
        document.getElementById("SmokeResult").style.display = "block";
    } else if (Math.max(Matteabouthue, SmokeNroses, Wineonly, Fadeintohue, Stonecoldfox) === Wineonly) {
        document.getElementById("WineResult").style.display = "block";
    } else if (Math.max(Matteabouthue, SmokeNroses, Wineonly, Fadeintohue, Stonecoldfox) === Fadeintohue) {
        document.getElementById("FadeResult").style.display = "block";
    } else if (Math.max(Matteabouthue, SmokeNroses, Wineonly, Fadeintohue, Stonecoldfox) === Stonecoldfox) {
        document.getElementById("Stonecoldresult").style.display = "block";
    }
}
