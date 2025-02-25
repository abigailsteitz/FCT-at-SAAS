// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function secretMessage() {
    alert("cupon code = mUSic. you get -$.25 off")
}
function displayXO() {
    document.getElementById("xoContent").style.display = "block";
    document.getElementById("eitherorContent").style.display = "none";
    document.getElementById("elliottContent").style.display = "none";
}
function displayeitheror() {
    document.getElementById("xoContent").style.display = "none";
    document.getElementById("eitherorContent").style.display = "block";
    document.getElementById("elliottContent").style.display = "none";
}
function redBackground() {
    document.body.style.backgroundColor = "red";
}