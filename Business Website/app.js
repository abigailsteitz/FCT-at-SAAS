// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function secretMessage() {
    alert("You found the secret message! Coupon code: #BuyaBag")
}
function citybag() {
    document.getElementById("cityContent").style.display = "block";
    document.getElementById("birkinContent").style.display = "none";
    document.getElementById("defaultContent").style.display = "none";
}
function birkin() {
    document.getElementById("cityContent").style.display = "none";
    document.getElementById("birkinContent").style.display = "block";
    document.getElementById("defaultContent").style.display = "none";
}
function greenBackground() {
    document.body.style.backgroundColor = "green";
}