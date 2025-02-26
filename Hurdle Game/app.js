// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

// The canvas is the black box we draw onto
var canvas = undefined; // Canvas set up when the document is done loading.
// The pen allows you to draw on the canvas
var pen = undefined; // Pen set up when the document is done loading.

// set up variables
var xPosition = 20;
var yPosition = 0;
var ySpeed = 0;
var hurdles = [];
var flyingObjects = [];
var bullets = [];
var bulletPowerUps = [];
var counter = 0;
var flyingCounter = 0;
var playing = true;
var playerSize = 30;
var hurdleSize = 50;
var flyingObjectSize = 30;
var lives = 3;
var bulletCount = 10;
var obstacleCounter = 0;

function drawSquare(xPosition, yPosition, size, color) {
    pen.beginPath();
    pen.rect(xPosition, yPosition, size, size);
    pen.fillStyle = color;
    pen.stroke();
    pen.fill();
}

function drawTextSquare(xPosition, yPosition, size, color, text) {
    pen.beginPath();
    pen.rect(xPosition, yPosition, size, size);
    pen.fillStyle = color;
    pen.stroke();
    pen.fill();
    pen.fillStyle = 'white';
    pen.font = '10px Arial';
    pen.fillText(text, xPosition + 5, yPosition + size / 2 + 3);
}

function drawBulldogFace(xPosition, yPosition, size) {
    // Draw the head
    pen.beginPath();
    pen.arc(xPosition + size / 2, yPosition + size / 2, size / 2, 0, Math.PI * 2, true);
    pen.fillStyle = 'cyan';
    pen.fill();
    pen.stroke();

    // Draw the eyes
    pen.beginPath();
    pen.arc(xPosition + size / 3, yPosition + size / 3, size / 10, 0, Math.PI * 2, true);
    pen.fillStyle = 'white';
    pen.fill();
    pen.stroke();

    pen.beginPath();
    pen.arc(xPosition + 2 * size / 3, yPosition + size / 3, size / 10, 0, Math.PI * 2, true);
    pen.fillStyle = 'white';
    pen.fill();
    pen.stroke();

    // Draw the pupils
    pen.beginPath();
    pen.arc(xPosition + size / 3, yPosition + size / 3, size / 20, 0, Math.PI * 2, true);
    pen.fillStyle = 'black';
    pen.fill();

    pen.beginPath();
    pen.arc(xPosition + 2 * size / 3, yPosition + size / 3, size / 20, 0, Math.PI * 2, true);
    pen.fillStyle = 'black';
    pen.fill();

    // Draw the nose
    pen.beginPath();
    pen.arc(xPosition + size / 2, yPosition + 2 * size / 3, size / 10, 0, Math.PI * 2, true);
    pen.fillStyle = 'black';
    pen.fill();
}

function keyDownHandler(e) {
    if (e.keyCode == 38) { // up arrow key
        if (yPosition >= (canvas.height - playerSize)) {
            ySpeed -= 17.5; // Higher jumps by 75%
        }
    } else if (e.keyCode == 82) { // 'r' for restart
        resetGame();
    } else if (e.keyCode == 32 && bulletCount > 0) { // space bar for shooting
        bullets.push({ xPosition: xPosition + playerSize, yPosition: yPosition + playerSize / 2 });
        bulletCount -= 1;
    }
}

addEventListener("keydown", keyDownHandler, false);

function updatePlayer() {
    ySpeed += 1.5; // Fall quicker but not by a lot
    yPosition += ySpeed;
    if (yPosition >= (canvas.height - playerSize)) {
        ySpeed = 0;
        yPosition = canvas.height - playerSize;
    }
    drawBulldogFace(xPosition, yPosition, playerSize);
}

function createHurdle() {
    var hurdle = {
        xPosition: canvas.width,
        yPosition: canvas.height - hurdleSize
    };
    hurdles.push(hurdle);
    obstacleCounter++;
    if (obstacleCounter % 7 === 0) {
        createBulletPowerUp();
    }
}

function createFlyingObject() {
    var flyingObject = {
        xPosition: canvas.width,
        yPosition: Math.random() * (canvas.height - playerSize - flyingObjectSize) + (canvas.height - playerSize - flyingObjectSize) // Lower to the ground
    };
    flyingObjects.push(flyingObject);
}

function createBulletPowerUp() {
    var bulletPowerUp = {
        xPosition: canvas.width,
        yPosition: canvas.height - 30 // Always on the ground, bigger size
    };
    bulletPowerUps.push(bulletPowerUp);
}

function updateHurdles() {
    if (counter <= 0) {
        createHurdle();
        counter = Math.floor(Math.random() * 100 + 50); // Less frequent hurdles
    }
    counter -= 1;
    for (var i = 0; i < hurdles.length; i++) {
        var hurdle = hurdles[i];
        hurdle.xPosition -= 7;
        drawSquare(hurdle.xPosition, hurdle.yPosition, hurdleSize, 'orange');
    }
}

function updateFlyingObjects() {
    if (flyingCounter <= 0) {
        createFlyingObject();
        flyingCounter = Math.floor(Math.random() * 100 + 50); // Less frequent flying objects
    }
    flyingCounter -= 1;
    for (var i = 0; i < flyingObjects.length; i++) {
        var flyingObject = flyingObjects[i];
        flyingObject.xPosition -= 7;
        drawSquare(flyingObject.xPosition, flyingObject.yPosition, flyingObjectSize, 'red');
    }
}

function updateBulletPowerUps() {
    for (var i = 0; i < bulletPowerUps.length; i++) {
        var bulletPowerUp = bulletPowerUps[i];
        bulletPowerUp.xPosition -= 7;
        drawTextSquare(bulletPowerUp.xPosition, bulletPowerUp.yPosition, 30, 'green', 'Bullet'); // Bigger size
    }
}

function updateBullets() {
    for (var i = 0; i < bullets.length; i++) {
        var bullet = bullets[i];
        bullet.xPosition += 10;
        drawSquare(bullet.xPosition, bullet.yPosition, 5, 'yellow');
    }
}

function checkCollision() {
    for (var i = 0; i < hurdles.length; i++) {
        var hurdle = hurdles[i];
        var playerLeft = xPosition;
        var playerRight = xPosition + playerSize;
        var playerTop = yPosition;
        var playerBottom = yPosition + playerSize;
        var hurdleLeft = hurdle.xPosition;
        var hurdleRight = hurdle.xPosition + hurdleSize;
        var hurdleTop = hurdle.yPosition;
        var hurdleBottom = hurdle.yPosition + hurdleSize;

        if (playerRight > hurdleLeft && playerLeft < hurdleRight && playerBottom > hurdleTop && playerTop < hurdleBottom) {
            lives -= 1;
            hurdles.splice(i, 1);
            if (lives <= 0) {
                playing = false;
            }
            break;
        }
    }

    for (var i = 0; i < flyingObjects.length; i++) {
        var flyingObject = flyingObjects[i];
        var playerLeft = xPosition;
        var playerRight = xPosition + playerSize;
        var playerTop = yPosition;
        var playerBottom = yPosition + playerSize;
        var flyingObjectLeft = flyingObject.xPosition;
        var flyingObjectRight = flyingObject.xPosition + flyingObjectSize;
        var flyingObjectTop = flyingObject.yPosition;
        var flyingObjectBottom = flyingObject.yPosition + flyingObjectSize;

        if (playerRight > flyingObjectLeft && playerLeft < flyingObjectRight && playerBottom > flyingObjectTop && playerTop < flyingObjectBottom) {
            lives -= 1;
            flyingObjects.splice(i, 1);
            if (lives <= 0) {
                playing = false;
            }
            break;
        }
    }

    for (var i = 0; i < bullets.length; i++) {
        var bullet = bullets[i];
        for (var j = 0; j < hurdles.length; j++) {
            var hurdle = hurdles[j];
            if (bullet.xPosition > hurdle.xPosition && bullet.xPosition < hurdle.xPosition + hurdleSize &&
                bullet.yPosition > hurdle.yPosition && bullet.yPosition < hurdle.yPosition + hurdleSize) {
                hurdles.splice(j, 1);
                bullets.splice(i, 1);
                i--;
                break;
            }
        }
        for (var j = 0; j < flyingObjects.length; j++) {
            var flyingObject = flyingObjects[j];
            if (bullet.xPosition > flyingObject.xPosition && bullet.xPosition < flyingObject.xPosition + flyingObjectSize &&
                bullet.yPosition > flyingObject.yPosition && bullet.yPosition < flyingObject.yPosition + flyingObjectSize) {
                flyingObjects.splice(j, 1);
                bullets.splice(i, 1);
                i--;
                break;
            }
        }
    }

    for (var i = 0; i < bulletPowerUps.length; i++) {
        var bulletPowerUp = bulletPowerUps[i];
        var playerLeft = xPosition;
        var playerRight = xPosition + playerSize;
        var playerTop = yPosition;
        var playerBottom = yPosition + playerSize;
        var powerUpLeft = bulletPowerUp.xPosition;
        var powerUpRight = bulletPowerUp.xPosition + 30; // Bigger size
        var powerUpTop = bulletPowerUp.yPosition;
        var powerUpBottom = bulletPowerUp.yPosition + 30; // Bigger size

        if (playerRight > powerUpLeft && playerLeft < powerUpRight && playerBottom > powerUpTop && playerTop < powerUpBottom) {
            bulletCount += 5;
            bulletPowerUps.splice(i, 1);
            break;
        }
    }
}

function update() {
    if (playing) {
        pen.clearRect(0, 0, canvas.width, canvas.height);
        updatePlayer();
        updateHurdles();
        updateFlyingObjects();
        updateBulletPowerUps();
        updateBullets();
        checkCollision();
        pen.font = "20px Arial";
        pen.fillStyle = "white";
        pen.fillText("Lives: " + lives, 10, 20);
        pen.fillText("Bullets: " + bulletCount, 10, 40);
    } else {
        pen.font = "30px Arial";
        pen.fillStyle = "red";
        pen.fillText("GAME OVER, press 'r' to restart", canvas.width / 2 - 150, canvas.height / 2);
    }
}

function initialSetup() {
    // set up canvas
    canvas = document.getElementById("canvas");
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;

    // set up the pen
    pen = canvas.getContext("2d");

    // Triggers the main function every 30 milliseconds
    setInterval(update, 30);
}

function resetGame() {
    hurdles = [];
    flyingObjects = [];
    bullets = [];
    bulletPowerUps = [];
    playing = true;
    lives = 3;
    bulletCount = 10;
    obstacleCounter = 0;
}

addEventListener("load", (event) => initialSetup());