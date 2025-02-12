// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("milkresult").style.display = "none";
    document.getElementById("saladresult").style.display = "none";
    document.getElementById("icecreamresult").style.display = "none";
    document.getElementById("frenchfryresult").style.display = "none";
    document.getElementById("frostedflakesresult").style.display = "none";
}
function seeResult() {
    var milk = 0;
    var salad = 0;
    var icecream = 0;
    var frenchfry = 0;
    var frostedflakes = 0;

    if (document.getElementById("redcolor").checked) {
        frenchfry += 1;
    } else if (document.getElementById("bluecolor").checked) {
        milk += 1;
        icecream += 1;
        frostedflakes += 1;
    } else {
       
        salad += 1;
    }

    if (document.getElementById("saltyflavor").checked) {
        frenchfry += 1;
    } else if (document.getElementById("sweetflavor").checked) {
        frostedflakes += 1;
        icecream  += 1;
    } else if (document.getElementById("sourflavor").checked) {
        salad  += 1;
        milk  += 1;
    } else {
        
    }

    if (document.getElementById("yesfridge").checked) {
        milk += 1;
        icecream += 1;
        salad += 1;
    } else if (document.getElementById("nofridge").checked) {
        frostedflakes += 1;

        frenchfry += 1;
    }

    if (document.getElementById("ketchuptopping").checked) {
        frenchfry += 1;
    } else if (document.getElementById("mustardtopping").checked) {
        icecream += 1;
        frostedflakes += 1;
    } else if (document.getElementById("ranchtopping").checked) {
        salad += 1;
    } else {
        // Use Diplomacy
        milk += 1;
    }

    if (document.getElementById("capitolonebank").checked) {
        frenchfry += 1;
    } else if (document.getElementById("chase").checked) {
        frostedflakes += 1;
    } else if (document.getElementById("bankofamerica").checked) {
        milk += 1;
        icecream += 1;
    } else {
        // Existential Crisis
        salad += 1;
    }

    resetResult();

    if (Math.max(frenchfry, milk, frostedflakes, icecream, salad) === frenchfry) {
        document.getElementById("frenchfryresult").style.display = "block";
    } else if (Math.max(frenchfry, milk, frostedflakes, icecream, salad) === milk) {
        document.getElementById("milkresult").style.display = "block";
    } else if (Math.max(frenchfry, milk, frostedflakes, icecream, salad) === salad) {
        document.getElementById("saladresult").style.display = "block";
    } else if (Math.max(frenchfry, milk, frostedflakes, icecream, salad) === frostedflakes) {
        document.getElementById("frostedflakesresult").style.display = "block";
    } else if (Math.max(frenchfry, milk, frostedflakes, icecream, salad) === icecream) {
        document.getElementById("icecreamresult").style.display = "block";
    }
}
