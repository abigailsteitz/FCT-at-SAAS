// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("AdventureResult").style.display = "none";
    document.getElementById("BookResult").style.display = "none";
    document.getElementById("GamerResult").style.display = "none";
    document.getElementById("BeachResult").style.display = "none";
    document.getElementById("MusicResult").style.display = "none";
}

function seeResult() {
    var Fish = 0;
    var Plankton = 0;
    var Nudibranch = 0;
    var Human = 0;
    var Spider = 0;

    if (document.getElementById("Adventure").checked) {
        Spider += 1;
    } else if (document.getElementById("Reading").checked) {
        Human += 1;
        Fish += 1;
        Nudibranch += 1;
    } else {
        Plankton += 1;
    }

    if (document.getElementById("Beach").checked) {
        Human += 1;
        Spider += 1;
        Nudibranch += 1;
    } else if (document.getElementById("Mountains").checked) {
        Fish += 1;
        Plankton += 1;
        Nudibranch += 1;
    } else {
        Nudibranch += 1;
    }

    if (document.getElementById("Sweet").checked) {
        Human += 1;
        Spider += 1;
    } else if (document.getElementById("Savory").checked) {
        Fish += 1;
        Plankton += 1;
        Nudibranch += 1;
    }

    if (document.getElementById("Think").checked) {
        Spider += 1;
    } else if (document.getElementById("Ask").checked) {
        Fish += 1;
        Plankton += 1;
    } else if (document.getElementById("Ignore").checked) {
        Nudibranch += 1;
    } else {
        Human += 1;
    }

    if (document.getElementById("Art").checked) {
        Spider += 1;
    } else if (document.getElementById("Music").checked) {
        Fish += 1;
    } else if (document.getElementById("Talking").checked) {
        Plankton += 1;
        Nudibranch += 1;
    } else {
        Human += 1;
    }

    resetResult();

    if (Math.max(Fish, Plankton, Human, Spider, Nudibranch) === Fish) {
        document.getElementById("AdventureResult").style.display = "block";
    } else if (Math.max(Fish, Plankton, Human, Spider, Nudibranch) === Plankton) {
        document.getElementById("BookResult").style.display = "block";
    } else if (Math.max(Fish, Plankton, Human, Spider, Nudibranch) === Human) {
        document.getElementById("GamerResult").style.display = "block";
    } else if (Math.max(Fish, Plankton, Human, Spider, Nudibranch) === Spider) {
        document.getElementById("BeachResult").style.display = "block";
    } else if (Math.max(Fish, Plankton, Human, Spider, Nudibranch) === Nudibranch) {
        document.getElementById("MusicResult").style.display = "block";
    }
}