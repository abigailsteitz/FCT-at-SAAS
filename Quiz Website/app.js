// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("Tennisresult").style.display = "none";
    document.getElementById("Bootresult").style.display = "none";
    document.getElementById("Flatresult").style.display = "none";
    document.getElementById("Slipperresult").style.display = "none";
    document.getElementById("Flipflopresult").style.display = "none";
}
function seeResult() {
    var Tennisresult = 0;
    var Bootresult = 0;
    var Slipperresult = 0;
    var Flatresult = 0;
    var Flipflopresult = 0;

    if (document.getElementById("3shoes").checked) {
        Tennisresult += 1;
    } else if (document.getElementById("2shoes").checked) {
        Bootresult += 1;
        Slipperresult += 1;
        Flatresult += 1;
    } else if (document.getElementById("5shoes").checked) {
        Flipflopresult += 1;
        // pairs of shoes had
        Tennisresult += 1;
    }

    if (document.getElementById("yes").checked) {
        Tennisresult += 1;
        Slipperresult += 1;
    } else if (document.getElementById("no").checked) {
        Bootresult += 1;
        Flatresult += 1;
        Tennisresult += 1;
    } else {
        // are you athletic
        Flipflopresult += 1;
    }

    if (document.getElementById("sunny").checked) {
        Tennisresult += 1;
        Bootresult += 1;
    } else if (document.getElementById("cold").checked) {
        Slipperresult += 1;
        Flatresult += 1;
        Flipflopresult += 1;
    }

    if (document.getElementById("Yes").checked) {
        Bootresult += 1;
    } else if (document.getElementById("No").checked) {
        Flatresult += 1;
        Slipperresult += 1;
    } else {
        // Use Diplomacy
        Flipflopresult += 1;
    }

    if (document.getElementById("0-10").checked) {
        Flipflopresult += 1;
    } else if (document.getElementById("11-14").checked) {
        Tennisresult += 1;
    } else if (document.getElementById("15-17").checked) {
        Bootresult += 1;
        Flatresult += 1;
    } else {
        // Existential Crisis
        Slipperresult += 1;
    }

    resetResult();

    if (Math.max(Tennisresult, Flipflopresult, Flatresult, Bootresult, Slipperresult) === Tennisresult) {
        document.getElementById("Tennisresult").style.display = "block";
    } else if (Math.max(Tennisresult, Flipflopresult, Flatresult, Bootresult, Slipperresult) === Flipflopresult) {
        document.getElementById("Flipflopresult").style.display = "block";
    } else if (Math.max(Tennisresult, Flipflopresult, Flatresult, Bootresult, Slipperresult) === Flatresult) {
        document.getElementById("Flatresult").style.display = "block";
    } else if (Math.max(Tennisresult, Flipflopresult, Flatresult, Bootresult, Slipperresult) === Bootresult) {
        document.getElementById("Bootresult").style.display = "block";
    } else if (Math.max(Tennisresult, Flipflopresult, Flatresult, Bootresult, Slipperresult) === Slipperresult) {
        document.getElementById("Slipperresult").style.display = "block";
    }
}
