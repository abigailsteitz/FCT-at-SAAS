// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("FishResult").style.display = "none";
    document.getElementById("PlanktonResult").style.display = "none";
    document.getElementById("HumanResult").style.display = "none";
    document.getElementById("SpiderResult").style.display = "none";
}
function seeResult() {
    var Fish = 0;
    var Plankton = 0;
    var Nudibranch = 0;
    var Human = 0;
    var Spider = 0;

    var question1 = document.querySelector('select[name="motivation"]').value;
    var question2 = document.querySelector('select[name="eyes"]').value;
    if (question1 == "personal_tragedy") {
        Spider += 1;
    } else {
        Plankton += 1;
    }

    if (question2 == "2Eyes") {
        Human += 1;
        Fish += 1;
        Nudibranch += 1;
    } else {
        Plankton += 1;
    }

    if (document.getElementById("Walk").checked) {
        Human += 1;
        Spider += 1;
        Nudibranch += 1;
    } else if (document.getElementById("Swim").checked) {
        Fish += 1;
        Plankton += 1;
        Nudibranch += 1;
    } else {
        // Swim upside down
        Nudibranch += 1;
    }

    if (document.getElementById("Yes").checked) {
        Human += 1;
        Spider += 1;
    } else if (document.getElementById("No").checked) {
        Fish += 1;
        Plankton += 1;
        Nudibranch += 1;
    }

    if (document.getElementById("Fight").checked) {
        Spider += 1;
    } else if (document.getElementById("Run").checked) {
        Fish += 1;
        Plankton += 1;
    } else if (document.getElementById("Secrete").checked) {
        Nudibranch += 1;
    } else {
        // Use Diplomacy
        Human += 1;
    }

    if (document.getElementById("Of course").checked) {
        Spider += 1;
    } else if (document.getElementById("Probably not").checked) {
        Fish += 1;
    } else if (document.getElementById("Head empty").checked) {
        Plankton += 1;
        Nudibranch += 1;
    } else {
        // Existential Crisis
        Human += 1;
    }

    resetResult();

    if (Math.max(Fish, Plankton, Human, Spider, Nudibranch) === Fish) {
        document.getElementById("BatmanResult").style.display = "block";
    } else if (Math.max(Fish, Plankton, Human, Spider, Nudibranch) === Plankton) {
        document.getElementById("SupermanResult").style.display = "block";
    } else if (Math.max(Fish, Plankton, Human, Spider, Nudibranch) === Human) {
        document.getElementById("SpidermanResult").style.display = "block";
    } else if (Math.max(Fish, Plankton, Human, Spider, Nudibranch) === Spider) {
        document.getElementById("CaptianamericanResult").style.display = "block";
    } else if (Math.max(Fish, Plankton, Human, Spider, Nudibranch) === Nudibranch) {
        document.getElementById("CaptianamericanResult").style.display = "block";
    }
}
