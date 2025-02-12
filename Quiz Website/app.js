// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("Healthy").style.display = "none";
    document.getElementById("VeryHealthy").style.display = "none";
    document.getElementById("NotHealthy").style.display = "none";
    document.getElementById("VeryNotHealthy").style.display = "none";
    document.getElementById("Average").style.display = "none"
}
function seeResult() {
    var Healthy = 0;
    var Very_Healthy = 0;
    var Average = 0;
    var Not_Healthy = 0;
    var Very_not_Healthy = 0;

    if (document.getElementById("2").checked) {
        Very_not_Healthy += 1;
    } else if (document.getElementById("1").checked) {
        Not_Healthy += 1;
        Healthy += 1;
        Average += 2;
    } else {
        // 1, 2, 3 or more depending on the species
        Very_Healthy += 1;
    }

    if (document.getElementById("4").checked) {
        Not_Healthy += 1;
        Very_not_Healthy += 1;
        Average += 1;
    } else if (document.getElementById("5").checked) {
        Healthy += 1;
        Average += 1;
    } else {
        // Swim upside down
        Very_Healthy += 1;
    }

    if (document.getElementById("8").checked) {
        Not_Healthy += 1;
        Very_not_Healthy += 1;
    } else if (document.getElementById("7").checked) {
        Healthy += 1;
        Very_Healthy += 2;
        Average += 1;
    }

    if (document.getElementById("9").checked) {
        Very_Healthy += 1;
    } else if (document.getElementById("10").checked) {
        Healthy += 1;
        Very_Healthy += 1;
    } else if (document.getElementById("12").checked) {
        Average += 1;
    } else {
        // Use Diplomacy
        Not_Healthy += 1;
    }

    if (document.getElementById("15").checked) {
        Very_not_Healthy += 1;
    } else if (document.getElementById("14").checked) {
        Average += 1;
    } else if (document.getElementById("13").checked) {
        Very_Healthy += 1;
        Healthy += 1;
    } else {
        // Existential Crisis
        Average += 1;
    }

    resetResult();

    if (Math.max(Healthy, Very_Healthy, Not_Healthy, Very_not_Healthy, Average) === Healthy) {
        document.getElementById("Healthy").style.display = "block";
    } else if (Math.max(Healthy, Very_Healthy, Not_Healthy, Very_not_Healthy, Average) === Very_Healthy) {
        document.getElementById("VeryHealthy").style.display = "block";
    } else if (Math.max(Healthy, Very_Healthy, Not_Healthy, Very_not_Healthy, Average) === Not_Healthy) {
        document.getElementById("NotHealthy").style.display = "block";
    } else if (Math.max(Healthy, Very_Healthy, Not_Healthy, Very_not_Healthy, Average) === Very_not_Healthy) {
        document.getElementById("VeryNotHealthy").style.display = "block";
    } else if (Math.max(Healthy, Very_Healthy, Not_Healthy, Very_not_Healthy, Average) === Average) {
        document.getElementById("Average").style.display = "block";
    }
}
