// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("quiz-form").addEventListener("submit", function (e) {
        e.preventDefault();

        const form = document.getElementById("quiz-form");
        const formData = new FormData(form);
        let piggyScore = 0;

        for (const [key, value] of formData.entries()) {
            if (value === "piggy") {
                piggyScore++;
            }
        }

        const resultDiv = document.getElementById("result");
        resultDiv.style.display = "block";

        if (piggyScore === 5) {
            resultDiv.innerHTML = "<h2>um maybe lay off the chips... and go outside, ur like 650lb</h2>";
        } else if (piggyScore >= 3) {
            resultDiv.innerHTML = "<h2>You are a TRUE pig! approx 400 pounds.</h2>";
        } else if (piggyScore === 2) {
            resultDiv.innerHTML = "<h2>id say youre about 300 pounds on a good day. nice.</h2>";
        } else if (piggyScore === 1) {
            resultDiv.innerHTML = "<h2>u an average pig, like 200lb</h2>";
        } else {
            resultDiv.innerHTML = "<h2>ur a little pig. about 2 pounds</h2>";
        }

        document.getElementById("home-button").style.display = "block";
    });
});
/* Your JavaScript code goes here */