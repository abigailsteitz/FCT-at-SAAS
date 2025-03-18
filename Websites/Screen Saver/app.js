// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

// The canvas is the black box we draw onto
var canvas = undefined; // Canvas set up when the document is done loading.
// the pen allows you to draw on the canvas
var pen = undefined; // Pen set up when the document is done loading.

// set up variables
var xPosition = 100;
var yPosition = 100;
var xSpeed = 1;
var size = 20;

// draws a square at position (x, y) with given size and color
function drawSquare(x, y, size, color) {
    pen.beginPath();
    pen.rect(x, y, size, size);
    pen.fillStyle = color;
    pen.stroke();
    pen.fill();
}

// checks for collisions and adjusts speed accordingly
function checkCollision() {
    if (xPosition > 200 - size) {
        xSpeed = -1;
    }
    // TODO: students should add another if statement here!
}

// main function, calls all the other functions
function update() {
    pen.clearRect(0, 0, canvas.width, canvas.height);
    xPosition += xSpeed;
    checkCollision()
    drawSquare(xPosition, yPosition, size, 'cyan');
}

function initialSetup() {
    // set up canvas
    canvas = document.getElementById("canvas");
    canvas.height = 200;
    canvas.width = 200;

    // set up the pen
    pen = canvas.getContext("2d");

    // Triggers the main function every 10 milliseconds
    setInterval(update, 10);
}

addEventListener("load", (event) => initialSetup());

/*
Step 1: Edit the code so that the square bounces off both the right side and the left side of the canvas - bouncing forever!

Step 2: Add a ySpeed variable to make the square move diagonally and bounce off the top and bottom too, like a traditional screen saver.

Optional challenges:
- Make the square change color everytime it bounces.
- Use a shape that is not a square.
- Add a second square.
- Count and display the number of bounces.
*/