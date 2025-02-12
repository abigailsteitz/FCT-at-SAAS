// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("BigHero6").style.display = "none";
    document.getElementById("Moana").style.display = "none";
    document.getElementById("FrozenII").style.display = "none";
    document.getElementById("Tarzan").style.display = "none";
    document.getElementById("ThePrincessandtheFrog").style.display = "none";
}
function seeResult() {
    var BigHero6 = 0;
    var Moana = 0;
    var FrozenII = 0;
    var Tarzan = 0;
    var ThePrincessandtheFrog = 0;

    if (document.getElementById("BeautyandtheBeast").checked) {
        ThePrincessandtheFrog += 1;
    } else if (document.getElementById("SleepingBeauty").checked) {
        Tarzan += 1;
        BigHero6 += 1;
        FrozenII += 1;
    } else {
        // 1, 2, 3 or more depending on the species
        Moana += 1;
    }

    if (document.getElementById("Olaf").checked) {
        Tarzan += 1;
        ThePrincessandtheFrog += 1;
        FrozenII += 1;
    } else if (document.getElementById("Baymax").checked) {
        BigHero6 += 1;
        Moana += 1;
        FrozenII += 1;
    } else {
        // Swim upside down
        FrozenII += 1;
    }

    if (document.getElementById("Ariel").checked) {
        Tarzan += 1;
        ThePrincessandtheFrog += 1;
    } else if (document.getElementById("SnowWhite").checked) {
        BigHero6 += 1;
        Moana += 1;
        FrozenII += 1;
    }

    if (document.getElementById("Pawpsicle").checked) {
        ThePrincessandtheFrog += 1;
    } else if (document.getElementById("Ratatouille").checked) {
        BigHero6 += 1;
        Moana += 1;
    } else {
        // Use Diplomacy
        Tarzan += 1;
        FrozenII += 1;
    }

    if (document.getElementById("LiShang").checked) {
        ThePrincessandtheFrog += 1;
    } else if (document.getElementById("Aladdin").checked) {
        BigHero6 += 1;
        Moana += 1;
   
    } else {
        // Existential Crisis
        Tarzan += 1;
        FrozenII += 1;
    }

    if (document.getElementById("DaisyDuck").checked) {
        ThePrincessandtheFrog += 1;
        Moana += 1;
    } else if (document.getElementById("MinnieMouse").checked) {
        BigHero6 += 1;
        Tarzan += 1;
   
    } else {
        // Existential Crisis
        FrozenII += 1;
    }

    resetResult();

    if (Math.max(BigHero6, Moana, Tarzan, ThePrincessandtheFrog, FrozenII) === BigHero6) {
        document.getElementById("BigHero6").style.display = "block";
    } else if (Math.max(BigHero6, Moana, Tarzan, ThePrincessandtheFrog, FrozenII) === Moana) {
        document.getElementById("Moana").style.display = "block";
    } else if (Math.max(BigHero6, Moana, Tarzan, ThePrincessandtheFrog, FrozenII) === Tarzan) {
        document.getElementById("FrozenII").style.display = "block";
    } else if (Math.max(BigHero6, Moana, Tarzan, ThePrincessandtheFrog, FrozenII) === ThePrincessandtheFrog) {
        document.getElementById("Tarzan").style.display = "block";
    } else if (Math.max(BigHero6, Moana, Tarzan, ThePrincessandtheFrog, FrozenII) === FrozenII) {
        document.getElementById("ThePrincessandtheFrog").style.display = "block";
    }
}
