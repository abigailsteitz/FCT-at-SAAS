// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';


var cart = [

];

/* Your JavaScript code goes here */
function addToCart(item) {

    // Pops up a dismissable window
    cart.push(item);
    alert(item + " added to your cart.");
}

document.addEventListener("DOMContentLoaded", function () {
    if (window.location.pathname.endsWith("cart.html")) {
        loadCart();
    }
});
function loadCart() {
    console.log("There are " + cart.length + " items in your cart.");
    for (item in cart) {
        console.log("item in cart: " + cart[item])
        var listItem = document.createElement("li");
        listItem.textContent = cart[item];
        document.getElementById("cart").appendChild(listItem);
    }

    console.log("loading cart");
}

function buy() {
    alert("Thank you for your purchase!");
}