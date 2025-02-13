'use strict';

function resetResult() {
    document.getElementById("PizzaResult").style.display = "none";
    document.getElementById("IceCreamResult").style.display = "none";
    document.getElementById("SteakResult").style.display = "none";
    document.getElementById("SushiResult").style.display = "none";
    document.getElementById("CurryResult").style.display = "none";
}

function seeResult() {
    var Pizza = 0;
    var IceCream = 0;
    var Steak = 0;
    var Sushi = 0;
    var Curry = 0;

    if (document.getElementById("Spicy").checked) {
        Curry += 1;
    } else if (document.getElementById("Sweet").checked) {
        IceCream += 1;
    } else if (document.getElementById("Savory").checked) {
        Pizza += 1;
        Steak += 1;
        Sushi += 1;
    }

    if (document.getElementById("Breakfast").checked) {
        IceCream += 1;
    } else if (document.getElementById("Lunch").checked) {
        Pizza += 1;
        Sushi += 1;
    } else if (document.getElementById("Dinner").checked) {
        Steak += 1;
        Curry += 1;
    }

    if (document.getElementById("Raw").checked) {
        Sushi += 1;
    } else if (document.getElementById("Grilled").checked) {
        Steak += 1;
    } else if (document.getElementById("Fried").checked) {
        Pizza += 1;
    }

    if (document.getElementById("Italian").checked) {
        Pizza += 1;
    } else if (document.getElementById("Mexican").checked) {
        Steak += 1;
    } else if (document.getElementById("Japanese").checked) {
        Sushi += 1;
    } else if (document.getElementById("Indian").checked) {
        Curry += 1;
    }

    if (document.getElementById("Very").checked) {
        Sushi += 1;
        Curry += 1;
    } else if (document.getElementById("Somewhat").checked) {
        Pizza += 1;
        Steak += 1;
    } else if (document.getElementById("NotAtAll").checked) {
        IceCream += 1;
    }

    resetResult();

    var maxScore = Math.max(Pizza, IceCream, Steak, Sushi, Curry);

    if (maxScore === Pizza) {
        document.getElementById("PizzaResult").style.display = "block";
    } else if (maxScore === IceCream) {
        document.getElementById("IceCreamResult").style.display = "block";
    } else if (maxScore === Steak) {
        document.getElementById("SteakResult").style.display = "block";
    } else if (maxScore === Sushi) {
        document.getElementById("SushiResult").style.display = "block";
    } else if (maxScore === Curry) {
        document.getElementById("CurryResult").style.display = "block";
    }
}
