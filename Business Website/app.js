// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function secretMessage() {
    alert("You found the secret message! Coupon code: #Football4Ever")
}
function displayDog() {
    document.body.style.backgroundColor = "Black"; 
    document.getElementById("dogContent").style.display = "block";
    document.getElementById("catContent").style.display = "none";
    document.getElementById("defaultContent").style.display = "none";
}
function displayCat() {
    document.body.style.backgroundColor = "Red"; 
    document.getElementById("dogContent").style.display = "none";
    document.getElementById("catContent").style.display = "block";
    document.getElementById("defaultContent").style.display = "none";
}
function Change() {
    document.body.style.backgroundColor = "Green"; 
}