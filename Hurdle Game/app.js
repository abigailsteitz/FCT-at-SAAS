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
var heartPowerUps = [];
var fuelPowerUps = [];
var counter = 0;
var flyingCounter = 0;
var playing = true;
var playerSize = 30;
var hurdleSize = 50;
var flyingObjectSize = 30;
var lives = 3;
var bulletCount = 10;
var obstacleCounter = 0;
var bulletPowerUpCounter = 0;
var fuelPowerUpCounter = 0;
var speedMultiplier = 1;
var levelUpMessage = false;
var levelUpTimer = 0;
var jetpackFuel = 7;
var jetpackActive = false;

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

function drawHeart(xPosition, yPosition, size, color) {
    pen.beginPath();
    pen.moveTo(xPosition + size / 2, yPosition + size / 4);
    pen.bezierCurveTo(xPosition + size / 2, yPosition, xPosition, yPosition, xPosition, yPosition + size / 4);
    pen.bezierCurveTo(xPosition, yPosition + size / 2, xPosition + size / 2, yPosition + size / 1.5, xPosition + size / 2, yPosition + size);
    pen.bezierCurveTo(xPosition + size / 2, yPosition + size / 1.5, xPosition + size, yPosition + size / 2, xPosition + size, yPosition + size / 4);
    pen.bezierCurveTo(xPosition + size, yPosition, xPosition + size / 2, yPosition, xPosition + size / 2, yPosition + size / 4);
    pen.fillStyle = color;
    pen.fill();
    pen.strokeStyle = 'blue';
    pen.lineWidth = 2;
    pen.stroke();
    pen.fillStyle = 'white';
    pen.font = '10px Arial';
    pen.fillText('1UP', xPosition + size / 4, yPosition + size / 1.5);
}

function drawFuelBox(xPosition, yPosition, size, color) {
    pen.beginPath();
    pen.rect(xPosition, yPosition, size, size);
    pen.fillStyle = color;
    pen.stroke();
    pen.fill();
    pen.fillStyle = 'white';
    pen.font = '10px Arial';
    pen.fillText('Fuel', xPosition + 5, yPosition + size / 2 + 3);
}

function drawFaceEmoji(xPosition, yPosition, size) {
    // Draw the head
    pen.beginPath();
    pen.arc(xPosition + size / 2, yPosition + size / 2, size / 2, 0, Math.PI * 2, true);
    pen.fillStyle = 'yellow';
    pen.fill();
    pen.stroke();

    // Draw the sunglasses
    pen.fillStyle = 'black';
    pen.fillRect(xPosition + size / 6, yPosition + size / 3, size / 3, size / 6);
    pen.fillRect(xPosition + size / 2, yPosition + size / 3, size / 3, size / 6);
    pen.fillRect(xPosition + size / 3, yPosition + size / 3, size / 3, size / 12);

    // Draw the mouth
    pen.beginPath();
    pen.arc(xPosition + size / 2, yPosition + 2 * size / 3, size / 6, 0, Math.PI, false);
    pen.stroke();
}

function keyDownHandler(e) {
    if (e.keyCode == 38) { // up arrow key
        if (yPosition >= (canvas.height - playerSize) && !jetpackActive) {
            ySpeed -= 20; // Higher jumps by 75% and longer in-air time
        }
    } else if (e.keyCode == 40 && jetpackFuel > 0) { // down arrow key for jetpack
        jetpackActive = true;
    } else if (e.keyCode == 82) { // 'r' for restart
        resetGame();
    } else if (e.keyCode == 32 && bulletCount > 0) { // space bar for shooting
        bullets.push({ xPosition: xPosition + playerSize, yPosition: yPosition + playerSize / 2 });
        bulletCount -= 1;
    }
}

addEventListener("keydown", keyDownHandler, false);

function keyUpHandler(e) {
    if (e.keyCode == 40) { // down arrow key for jetpack
        jetpackActive = false;
    }
}

addEventListener("keyup", keyUpHandler, false);

function updatePlayer() {
    if (jetpackActive && jetpackFuel > 0) {
        jetpackFuel -= 1 / 30; // 1 fuel per second
        ySpeed = -5; // Fly upwards
    } else {
        jetpackActive = false;
        ySpeed += 1.2; // Fall slower for longer in-air time
    }
    yPosition += ySpeed;
    if (yPosition >= (canvas.height - playerSize)) {
        ySpeed = 0;
        yPosition = canvas.height - playerSize;
    }
    drawFaceEmoji(xPosition, yPosition, playerSize);
}

function createHurdle() {
    var hurdle = {
        xPosition: canvas.width,
        yPosition: canvas.height - hurdleSize
    };
    hurdles.push(hurdle);
    obstacleCounter++;
    if (obstacleCounter % 10 === 0) {
        createBulletPowerUp();
    }
}

function createFlyingObject() {
    var flyingObject = {
        xPosition: canvas.width,
        yPosition: Math.random() * (canvas.height - playerSize - flyingObjectSize - 50) + (canvas.height - playerSize - flyingObjectSize - 50) // Higher spawn point
    };
    flyingObjects.push(flyingObject);
}

function createBulletPowerUp() {
    var bulletPowerUp = {
        xPosition: canvas.width,
        yPosition: canvas.height - 30 // Always on the ground, bigger size
    };
    bulletPowerUps.push(bulletPowerUp);
    bulletPowerUpCounter++;
    if (bulletPowerUpCounter % 2 === 0) {
        setTimeout(createHeartPowerUp, 1000); // Create heart power-up shortly after bullet power-up
    }
    if (bulletPowerUpCounter % 3 === 0) {
        setTimeout(createFuelPowerUp, 2000); // Create fuel power-up shortly after bullet power-up
    }
}

function createHeartPowerUp() {
    var heartPowerUp = {
        xPosition: canvas.width,
        yPosition: canvas.height - 30 // Always on the ground
    };
    heartPowerUps.push(heartPowerUp);
}

function createFuelPowerUp() {
    var fuelPowerUp = {
        xPosition: canvas.width,
        yPosition: canvas.height - 30 // Always on the ground
    };
    fuelPowerUps.push(fuelPowerUp);
}

function updateHurdles() {
    if (counter <= 0) {
        createHurdle();
        counter = Math.floor(Math.random() * 100 + 50); // Less frequent hurdles
    }
    counter -= 1;
    for (var i = 0; i < hurdles.length; i++) {
        var hurdle = hurdles[i];
        hurdle.xPosition -= 7 * speedMultiplier;
        drawSquare(hurdle.xPosition, hurdle.yPosition, hurdleSize, 'orange');
    }
}

function updateFlyingObjects() {
    if (flyingCounter <= 0) {
        createFlyingObject();
        flyingCounter = Math.floor(Math.random() * 50 + 25); // More frequent flying objects
    }
    flyingCounter -= 1;
    for (var i = 0; i < flyingObjects.length; i++) {
        var flyingObject = flyingObjects[i];
        flyingObject.xPosition -= 7 * speedMultiplier;
        drawSquare(flyingObject.xPosition, flyingObject.yPosition, flyingObjectSize, 'red');
    }
}

function updateBulletPowerUps() {
    for (var i = 0; i < bulletPowerUps.length; i++) {
        var bulletPowerUp = bulletPowerUps[i];
        bulletPowerUp.xPosition -= 7 * speedMultiplier;
        drawTextSquare(bulletPowerUp.xPosition, bulletPowerUp.yPosition, 30, 'green', 'Bullet'); // Bigger size
    }
}

function updateHeartPowerUps() {
    for (var i = 0; i < heartPowerUps.length; i++) {
        var heartPowerUp = heartPowerUps[i];
        heartPowerUp.xPosition -= 7 * speedMultiplier;
        drawHeart(heartPowerUp.xPosition, heartPowerUp.yPosition, 30, 'green');
    }
}

function updateFuelPowerUps() {
    for (var i = 0; i < fuelPowerUps.length; i++) {
        var fuelPowerUp = fuelPowerUps[i];
        fuelPowerUp.xPosition -= 7 * speedMultiplier;
        drawFuelBox(fuelPowerUp.xPosition, fuelPowerUp.yPosition, 30, 'white');
    }
}

function updateBullets() {
    for (var i = 0; i < bullets.length; i++) {
        var bullet = bullets[i];
        bullet.xPosition += 10 * speedMultiplier;
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

    for (var i = 0; i < heartPowerUps.length; i++) {
        var heartPowerUp = heartPowerUps[i];
        var playerLeft = xPosition;
        var playerRight = xPosition + playerSize;
        var playerTop = yPosition;
        var playerBottom = yPosition + playerSize;
        var heartLeft = heartPowerUp.xPosition;
        var heartRight = heartPowerUp.xPosition + 30;
        var heartTop = heartPowerUp.yPosition;
        var heartBottom = heartPowerUp.yPosition + 30;

        if (playerRight > heartLeft && playerLeft < heartRight && playerBottom > heartTop && playerTop < heartBottom) {
            lives += 1;
            heartPowerUps.splice(i, 1);
            xPosition = 20; // Reset player position to start
            speedMultiplier += 0.1; // Increase speed
            levelUpMessage = true;
            levelUpTimer = 45; // 1.5 seconds at 30 FPS
            break;
        }
    }

    for (var i = 0; i < fuelPowerUps.length; i++) {
        var fuelPowerUp = fuelPowerUps[i];
        var playerLeft = xPosition;
        var playerRight = xPosition + playerSize;
        var playerTop = yPosition;
        var playerBottom = yPosition + playerSize;
        var fuelLeft = fuelPowerUp.xPosition;
        var fuelRight = fuelPowerUp.xPosition + 30;
        var fuelTop = fuelPowerUp.yPosition;
        var fuelBottom = fuelPowerUp.yPosition + 30;

        if (playerRight > fuelLeft && playerLeft < fuelRight && playerBottom > fuelTop && playerTop < fuelBottom) {
            jetpackFuel += 1;
            fuelPowerUps.splice(i, 1);
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
        updateHeartPowerUps();
        updateFuelPowerUps();
        updateBullets();
        checkCollision();
        pen.font = "30px Arial"; // Bigger font size
        pen.fillStyle = "white";
        pen.fillText("Lives: " + lives, 10, 30);
        pen.fillText("Bullets: " + bulletCount, 10, 60);
        pen.fillText("Fuel: " + Math.floor(jetpackFuel), 10, 90);
        if (levelUpMessage) {
            pen.font = "40px Arial";
            pen.fillStyle = "yellow";
            pen.strokeStyle = "red";
            pen.lineWidth = 3;
            pen.strokeText("LEVEL UP", canvas.width / 2 - 100, 50);
            pen.fillText("LEVEL UP", canvas.width / 2 - 100, 50);
            levelUpTimer--;
            if (levelUpTimer <= 0) {
                levelUpMessage = false;
            }
        }
    } else {
        pen.font = "30px Arial";
        pen.fillStyle = "red";
        pen.fillText("GAME OVER, press 'r' to restart", canvas.width / 2 - 150, canvas.height / 2);
    }
}

function initialSetup() {
    // set up canvas
    canvas = document.getElementById("canvas");
    canvas.height = window.innerHeight * 0.85; // Take up 85% of the window height
    canvas.width = window.innerWidth;

    // set up the pen
    pen = canvas.getContext("2d");

    // Triggers the main function every 30 milliseconds
    setInterval(update, 30);

    // Speed up the game every 15 seconds
    setInterval(() => {
        speedMultiplier += 0.1;
    }, 15000);
}

function resetGame() {
    hurdles = [];
    flyingObjects = [];
    bullets = [];
    bulletPowerUps = [];
    heartPowerUps = [];
    fuelPowerUps = [];
    playing = true;
    lives = 3;
    bulletCount = 10;
    obstacleCounter = 0;
    bulletPowerUpCounter = 0;
    fuelPowerUpCounter = 0;
    speedMultiplier = 1;
    xPosition = 20;
    levelUpMessage = false;
    levelUpTimer = 0;
    jetpackFuel = 7;
    jetpackActive = false;
}

addEventListener("load", (event) => initialSetup());