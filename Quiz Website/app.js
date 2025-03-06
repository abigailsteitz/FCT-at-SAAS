// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("FishResult").style.display = "none";
    document.getElementById("PlanktonResult").style.display = "none";
    document.getElementById("HumanResult").style.display = "none";
    document.getElementById("SpiderResult").style.display = "none";
}

function seeResult() {
    var Kounde = 0;
    var Barcola = 0;
    var Marmoosh = 0;
    var Olise = 0;

    if (document.getElementById("8Eyes").checked) {
        Olise += 1;
    } else if (document.getElementById("2Eyes").checked) {
        Kounde += 1;
    } else {
        // 1, 2, 3 or more depending on the species
        Marmoosh += 1;
        Barcola += 1;
    }

    if (document.getElementById("Walk").checked) {
        Barcola += 1;
    } else if (document.getElementById("Swim").checked) {
        Marmoosh += 1;
    } else if (document.getElementById("SwimupsideDown").checked) {
        Olise += 1;
    } else {
        // Fixed incorrect variable name (Barcalona → Barcola)
        Barcola += 1;
    }

    if (document.getElementById("Yes").checked) {
        Marmoosh += 1;
        Barcola += 1;
    } else if (document.getElementById("No").checked) {
        Kounde += 1;
        Olise += 1;
    }

    if (document.getElementById("Fight").checked) {
        Barcola += 1;
    } else if (document.getElementById("Run").checked) {
        Olise += 1;
    } else if (document.getElementById("Secrete").checked) {
        Marmoosh += 1;
    } else {
        // Use Diplomacy
        Kounde += 1;
    }

    if (document.getElementById("Of course").checked) {
        Barcola += 1;
    } else if (document.getElementById("Probably not").checked) {
        Olise += 1;
    } else if (document.getElementById("Head empty").checked) {
        Kounde += 1;
    } else {
        // Existential Crisis
        Marmoosh += 1;
    }

    resetResult();

    let maxScore = Math.max(Barcola, Marmoosh, Olise, Kounde);

    if (maxScore === Barcola) {
        document.getElementById("FishResult").style.display = "block";
    } else if (maxScore === Marmoosh) {
        document.getElementById("PlanktonResult").style.display = "block";
    } else if (maxScore === Olise) {
        document.getElementById("HumanResult").style.display = "block";
    } else if (maxScore === Kounde) {
        document.getElementById("SpiderResult").style.display = "block";
    }
}
