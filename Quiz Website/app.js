// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    document.getElementById("Catresult").style.display = "none";
    document.getElementById("Owlresult").style.display = "none";
    document.getElementById("Jellyfishresult").style.display = "none";
}
function seeResult() {
    var Cat = 0;
    var Jellyfish = 0;
    var Owl = 0;


    if (document.getElementById("Quiet").checked) {
        Cat += 1;
    } else if (document.getElementById("Chill").checked) {
        Owl += 1;
    } else if (document.getElementById("Jellyfish").checked) {
        // 1, 2, 3 or more depending on the species
        Jellyfish += 1;
    }

    if (document.getElementById("Pink").checked) {
        Cat += 1;
    } else if (document.getElementById("Blue").checked) {
        Jellyfish += 1;
    } else if (document.getElementById("Neutrals").checked) {
     Owl += 1;

    }

    if (document.getElementById("English").checked) {
        Cat += 1;
    } else if (document.getElementById("Music").checked) {
        Owl += 1;
    } else if (document.getElementById("School whats that").checked) {
        Jellyfish += 1;

    }

    if (document.getElementById("HYPERPIGMENTATION").checked) {
        Cat += 1;
    } else if (document.getElementById("Raise your ya ya ya").checked) {
        Owl += 1;
    } else if (document.getElementById("Purple heart or whatever").checked) {
        Jellyfish += 1;
    
    }

    if (document.getElementById("True Blue - Boygenius").checked) {
        Cat += 1;
    } else if (document.getElementById("Gypsy - Fleetwood Mac").checked) {
        Owl += 1;
    } else if (document.getElementById("Carey - Joni Mitchell").checked) {
        Jellyfish += 1;

    }

    resetResult();

    if (Math.max(Cat, Owl, Jellyfish) === Cat) {
        document.getElementById("Catresult").style.display = "block";
    } else if (Math.max(Cat, Owl, Jellyfish) === Owl) {
        document.getElementById("Owlresult").style.display = "block";
    } else if (Math.max(Cat, Owl, Jellyfish) === Jellyfish) {

    }
}
