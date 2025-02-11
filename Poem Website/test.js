// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

let CONST_PASS = "yeppers"
let CONST_FAIL = "nopers"
let CONST_TESTNOTRUN = "Test not run"

let tests = [
    {
        name: "Update the title",
        originalValueInCode: "A Love Haiku to my Puppy-Dog",
        getValueFunc: () => document.getElementById("title").innerText,
        result: CONST_TESTNOTRUN
    },
    {
        name: "Change the poem",
        originalValueInCode: "Romeo is my",
        getValueFunc: () => {
            let poem = document.getElementById('poem')
            return poem.innerText.slice(0, 11)
        },
        result: CONST_TESTNOTRUN
    },
    {
        name: "Change the picture",
        originalValueInCode: "Romeo&Luna.jpg",
        getValueFunc: () => {
            let pic = document.getElementById('poemPic')
            // Get the last characters of the string to avoid the full file path
            return pic.src.substr(pic.src.length - 14)
        },
        result: CONST_TESTNOTRUN
    },
    {
        name: "Change the background color",
        originalValueInCode: "hsla(323, 78.80%, 87.10%, 0.30)",
        getValueFunc: () => {
            let bodyStyle = window.getComputedStyle(document.body);
            return bodyStyle.backgroundColor;
        },
        result: CONST_TESTNOTRUN
    },
]

function displayTests() {
    let content = document.getElementById("testCollapsibleContent")
    if (content.style.display === "block") {
        content.style.display = "none";
    } else {
        content.style.display = "block";
    }
}

function runTests() {
    // Reset results from last time
    let resultsElement = document.getElementById("results")
    resultsElement.innerHTML = ""

    document.getElementById("level2").style.display = "none";
    document.getElementById("level3").style.display = "none";

    // A for loop to go through each test in the list of tests
    for (const test of tests) {
        // Run the test
        let value = test.getValueFunc()
        if (value === test.originalValueInCode) {
            test.result = CONST_FAIL
        } else {
            test.result = CONST_PASS
        }

        // Create results paragraph tag
        let result = `<p class="result ${test.result}">Test: ${test.name}, Result: ${test.result}</p>`

        // Add result to HTML document
        resultsElement.innerHTML += result
    };

    // If they got all the requirements, the skills shown are Level 3 on this assignment.
    let didAllPass = tests.every(test => test.result === CONST_PASS)

    if (didAllPass === true) {
        document.getElementById("level3").style.display = "block";
    } else {
        document.getElementById("level2").style.display = "block";
    }
}