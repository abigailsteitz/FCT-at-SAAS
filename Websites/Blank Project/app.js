// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

/* Gets the cart object from browser storage */
function getCart() {
    const storedCart = sessionStorage.getItem('cart');
    return storedCart ? JSON.parse(storedCart) : [];
}

/* Adds an item to the cart in browser storage */
function addItem(item) {
    var cart = getCart();
    cart.push(item);
    sessionStorage.setItem('cart', JSON.stringify(cart));
}

/* HTML pages should call this function to add an item to the cart */
function addToCart(item) {

    // Pops up a dismissable window
    addItem(item);
    alert(item + " added to your cart.");
}

/* When the cart page loads, adds items to HTML */
document.addEventListener("DOMContentLoaded", function () {
    if (window.location.pathname.endsWith("cart.html")) {
        loadCart();
    }
});

function buy() {
    alert("Thank you for your purchase!");
    sessionStorage.setItem('cart', JSON.stringify({}));
    window.location.href = "thankYou.html";
}

function loadCart() {
    console.log("There are " + cart.length + " items in your cart.");
    for (var item of getCart()) {
        console.log("item in cart: " + item)
        var listItem = document.createElement("li");
        listItem.textContent = item;
        document.getElementById("cart").appendChild(listItem);
    }

    console.log("loading cart");
}

