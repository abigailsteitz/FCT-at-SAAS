'use strict';

function resetResult() {
    document.getElementById("BlackHoodie").style.display = "none";
    document.getElementById("BlackSweatshirt").style.display = "none";
    document.getElementById("WhiteSweatshirt").style.display = "none";
    document.getElementById("WhiteTank").style.display = "none";
    document.getElementById("BlackJeans").style.display = "none";
    document.getElementById("BlueJeans").style.display = "none";
    document.getElementById("BlackShorts").style.display = "none";
    document.getElementById("BlueShorts").style.display = "none";
    document.getElementById("Hat").style.display = "none";
}
function seeResult() {
    var BlackHoodieScore = 0;
    var BlackSweatshirtScore = 0;
    var WhiteSweatshirtScore = 0;
    var WhiteTankScore = 0;
    var BlackJeansScore = 0;
    var BlueJeansScore = 0;
    var BlackShortsScore = 0;
    var BlueShortsScore = 0;
    var HatScore = 0;

    if (document.getElementById("Pants").checked) {
        BlackJeansScore += 1;
        BlueJeansScore += 1;
        BlueShortsScore += 1;
        BlackShortsScore += 1;
    } else if (document.getElementById("Top").checked) {
        BlackHoodieScore += 1;
        WhiteSweatshirtScore += 1;
        BlackSweatshirtScore += 1;
        WhiteTankScore += 1;
    } else if (document.getElementById("Accessories").checked) {
        HatScore += 1;
    }

    if (document.getElementById("Black").checked) {
        BlackHoodieScore += 1;
        BlackJeansScore += 1;
        BlackShortsScore += 1;
        BlackSweatshirtScore += 1;
        WhiteSweatshirtScore = 0;
        WhiteTankScore = 0;
        BlueJeansScore = 0;
        BlueShortsScore = 0;
        HatScore = 0;
    } else if (document.getElementById("White").checked) {
        WhiteSweatshirtScore += 1;
        WhiteTankScore += 1;
        BlackJeansScore = 0;
        BlackShortsScore = 0;
        BlackSweatshirtScore = 0;
        BlueJeansScore = 0;
        BlueShortsScore = 0;
        HatScore = 0;
    } else if (document.getElementById("Blue").checked) {
        BlueJeansScore += 1;
        BlueShortsScore += 1;
        HatScore += 1;
        WhiteSweatshirtScore = 0;
        WhiteTankScore = 0;
        BlackHoodieScore = 0;
        BlackJeansScore = 0;
        BlackShortsScore = 0;
        BlackSweatshirtScore = 0;
    }

    if (document.getElementById("Cool").checked) {
        BlackHoodieScore += 1;
        BlackSweatshirtScore += 1;
        WhiteSweatshirtScore += 1;
        BlackJeansScore += 1;
        BlueJeansScore += 1;
        WhiteTankScore = 0;
        BlueShortsScore = 0;
        BlackShortsScore = 0;
    } else if (document.getElementById("Warm").checked) {
        WhiteTankScore = 1;
        BlueShortsScore += 1;
        BlackShortsScore += 1;
        BlackHoodieScore = 0;
        BlackSweatshirtScore = 0;
        WhiteSweatshirtScore = 0;
        BlackJeansScore = 0;
        BlueJeansScore = 0;
        HatScore = 0;
    } else if (document.getElementById("All").checked) {
        HatScore += 1;
        WhiteTankScore = 0;
        BlueShortsScore = 0;
        BlackShortsScore = 0;
        BlackHoodieScore = 0;
        BlackSweatshirtScore = 0;
        WhiteSweatshirtScore = 0;
        BlackJeansScore = 0;
        BlueJeansScore = 0;
    }

    if (document.getElementById("No").checked) {
        BlackHoodieScore += 1;
        BlueJeansScore += 1;
        BlackJeansScore += 1;
        BlackShortsScore += 1;
        BlueShortsScore += 1;
        HatScore += 1;
        WhiteTankScore += 1;
        BlackSweatshirtScore = 0;
        WhiteSweatshirtScore = 0;
    } else if (document.getElementById("Yes").checked) {
        BlackSweatshirtScore += 1;
        WhiteSweatshirtScore += 1;
        BlackHoodieScore = 0;
        BlueJeansScore = 0;
        BlackJeansScore = 0;
        BlackShortsScore = 0;
        BlueShortsScore = 0;
        HatScore = 0;
        WhiteTankScore = 0;
    }

    if (document.getElementById("Cover").checked) {
        HatScore += 1;
        BlackHoodieScore += 1;
        WhiteSweatshirtScore = 0;
        BlackSweatshirtScore = 0;
        BlueJeansScore = 0;
        BlackJeansScore = 0;
        BlueShortsScore = 0;
        BlackShortsScore = 0
        WhiteTankScore = 0;
    } else if (document.getElementById("NoCover").checked) {
        WhiteSweatshirtScore += 1;
        BlackSweatshirtScore += 1;
        BlueJeansScore += 1;
        BlackJeansScore += 1;
        BlueShortsScore += 1;
        BlackShortsScore += 1;
        WhiteTankScore += 1;
        HatScore = 0;
        BlackHoodieScore = 0;
    }

    resetResult();

    var HighestScore = Math.max(BlackHoodieScore, BlackSweatshirtScore, WhiteSweatshirtScore, WhiteTankScore, BlackJeansScore, BlueJeansScore, BlackShortsScore, BlueShortsScore, HatScore);
    if (HighestScore === BlackHoodieScore) {
        document.getElementById("BlackHoodie").style.display = "block";
    } else if (HighestScore === BlackSweatshirtScore) {
        document.getElementById("BlackSweatshirt").style.display = "block";
    } else if (HighestScore === WhiteSweatshirtScore) {
        document.getElementById("WhiteSweatshirt").style.display = "block";
    } else if (HighestScore === WhiteTankScore) {
        document.getElementById("WhiteTank").style.display = "block";
    } else if (HighestScore === BlackJeansScore) {
        document.getElementById("BlackJeans").style.display = "block";
    } else if (HighestScore === BlueJeansScore) {
        document.getElementById("BlueJeans").style.display = "block";
    } else if (HighestScore === BlackShortsScore) {
        document.getElementById("BlackShorts").style.display = "block";
    } else if (HighestScore === BlueShortsScore) {
        document.getElementById("BlueShorts").style.display = "block";
    } else if (HighestScore === HatScore) {
        document.getElementById("Hat").style.display = "block";
    }
}
