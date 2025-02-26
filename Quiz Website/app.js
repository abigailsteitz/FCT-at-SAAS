// Switch to strict mode to get more useful errors when you make mistakes.
'use strict';

function resetResult() {
    
    document.getElementById("HumanResult").style.display = "none";
    document.getElementById("SpiderResult").style.display = "none";
}
function seeResult() {
  
 

    var Human = 0;
    var Spider = 0;

    if (document.getElementById("8Eyes").checked) {
        Spider += 1;
    } else if (document.getElementById("2Eyes").checked) {
        Human += 1;
       
    } else {
        // 1, 2, 3 or more depending on the species
     
    }

    if (document.getElementById("Walk").checked) {
        Human += 1;
        Spider += 1;
       
    } else if (document.getElementById("Swim").checked) {
      
        
    } else {
        // Swim upside down
       
    }

    if (document.getElementById("Yes").checked) {
        Human += 1;
        Spider += 1;
    } else if (document.getElementById("No").checked) {
     
    }

    if (document.getElementById("Fight").checked) {
        Spider += 1;
    } else if (document.getElementById("Run").checked) {
        
    } else if (document.getElementById("Secrete").checked) {
     
    } else {
        // Use Diplomacy
        Human += 1;
    }

    if (document.getElementById("Of course").checked) {
        Spider += 1;
    } else if (document.getElementById("Probably not").checked) {
    
    } else if (document.getElementById("Head empty").checked) {
        
    } else {
        // Existential Crisis
        Human += 1;
    }

    resetResult();

    
    
    if (Math.max( Human, Spider) === Human) {
        document.getElementById("HumanResult").style.display = "block";
    } else if (Math.max( Human, Spider) === Spider) {
        document.getElementById("SpiderResult").style.display = "block";
    }
}
