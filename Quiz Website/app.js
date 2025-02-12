// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("EagleResult").style.display = "none";
    document.getElementById("Barnicalresult").style.display = "none";
    document.getElementById("MutantResult").style.display = "none";
    document.getElementById("penguinResult").style.display = "none";
}
function seeResult() {
    var Eagle = 0;
    var Barnicle = 0;
    var dumpling = 0;
    var Mutant = 0;
    var penguin = 0;

    if (document.getElementById("Fruit").checked) {
        penguin += 1;
    } else if (document.getElementById("Vegtables").checked) {
        Mutant += 1;
        Eagle += 1;
        dumpling += 1;
    } else {
        // 1, 2, 3 or more depending on the species
        Barnicle += 1;
    }

    if (document.getElementById("Walk").checked) {
        Mutant += 1;
        penguin += 1;
        dumpling += 1;
    } else if (document.getElementById("Swim").checked) {
        Eagle += 1;
        Barnicle += 1;
        dumpling += 1;
    } else {
        // Swim upside down
        dumpling += 1;
    }

    if (document.getElementById("Yes").checked) {
        Mutant += 1;
        penguin += 1;
    } else if (document.getElementById("No").checked) {
        Eagle += 1;
        Barnicle += 1;
        dumpling += 1;
    }

    if (document.getElementById("Fight").checked) {
        penguin += 1;
    } else if (document.getElementById("Run").checked) {
        Eagle += 1;
        Barnicle += 1;
    } else if (document.getElementById("Secrete").checked) {
        dumpling += 1;
    } else {
        // Use Diplomacy
        Mutant += 1;
    }

    if (document.getElementById("Of course").checked) {
        penguin += 1;
    } else if (document.getElementById("Probably not").checked) {
        Eagle += 1;
    } else if (document.getElementById("Head empty").checked) {
        Barnicle += 1;
        dumpling += 1;
    } else {
        // Existential Crisis
        Mutant += 1;
    }

    resetResult();

    if (Math.max(Eagle, Barnicle, Mutant, penguin, dumpling) === Eagle) {
        document.getElementById("EagleResult").style.display = "block";
    } else if (Math.max(Eagle, Barnicle, Mutant, penguin, dumpling) === Barnicle) {
        document.getElementById("Barnicalresult").style.display = "block";
    } else if (Math.max(Eagle, Barnicle, Mutant, penguin, dumpling) === Mutant) {
        document.getElementById("MutantResult").style.display = "block";
    } else if (Math.max(Eagle, Barnicle, Mutant, penguin, dumpling) === penguin) {
        document.getElementById("penguinResult").style.display = "block";
    } else if (Math.max(Eagle, Barnicle, Mutant, penguin, dumpling) === dumpling) {
        document.getElementById("dumplingresult").style.display = "block";
    }
}
