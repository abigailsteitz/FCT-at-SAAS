// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("ForeignerResult").style.display = "none";
    document.getElementById("DumbResult").style.display = "none";
    document.getElementById("NerdResult").style.display = "none";
    document.getElementById("AmericanResult").style.display = "none";
}
function seeResult() {
    var Foreigner = 0;
    var Dumb = 0;
    var Nerd = 0;
    var American = 0;

    if (document.getElementById("50").checked) {
        American += 1;
    } else if (document.getElementById("Solid").checked) {
        Nerd += 1;
    } else {
        // 51
        Dumb += 1;
        Foreigner += 1;
    }

    if (document.getElementById("Lincoln").checked) {
        Dumb += 1;
    } else if (document.getElementById("Trump").checked) {
        American += 1;
        Nerd += 1;
    } else {
        // Barack Obama
        Foreigner += 1;
    }

    if (document.getElementById("Yes").checked) {
        Dumb += 1;
        American += 1;
    } else if (document.getElementById("No").checked) {
        Nerd += 1;
        Foreigner += 1;
    }

    if (document.getElementById("DC").checked) {
        American += 1;
    } else if (document.getElementById("NY").checked) {
        Foreigner += 1;
    } else if (document.getElementById("olal").checked) {
        Nerd += 1;
    } else {
        // bro i have no clue
        Dumb += 1;
    }

    if (document.getElementById("solo").checked) {
        Foreigner += 1;
    } else if (document.getElementById("canadamexico").checked) {
        American += 1;
    } else if (document.getElementById("us").checked) {
        Dumb += 1;
    } else {
        // Existential Crisis
        Nerd += 1;
    }

    resetResult();

    if (Math.max(Foreigner, Dumb, Nerd, American) === Foreigner) {
        document.getElementById("ForeignerResult").style.display = "block";
    } else if (Math.max(Foreigner, Dumb, Nerd, American) === Dumb) {
        document.getElementById("DumbResult").style.display = "block";
    } else if (Math.max(Foreigner, Dumb, Nerd, American) === Nerd) {
        document.getElementById("NerdResult").style.display = "block";
    } else if (Math.max(Foreigner, Dumb, Nerd, American) === American) {
        document.getElementById("AmericanResult").style.display = "block";
    }
}
