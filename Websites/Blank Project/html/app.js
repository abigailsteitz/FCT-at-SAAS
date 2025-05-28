// Add a welcome message with animation
document.getElementById("welcomeButton").addEventListener("click", function () {
  const message = document.getElementById("welcomeMessage");
  message.textContent = "🎉 Welcome to KeyFix! We're here to make your typing experience smooth and hassle-free. 🎉";
  message.classList.remove("hidden");
  message.style.opacity = 0;

  // Fade-in animation
  let opacity = 0;
  const fadeIn = setInterval(() => {
    if (opacity >= 1) {
      clearInterval(fadeIn);
    } else {
      opacity += 0.05;
      message.style.opacity = opacity;
    }
  }, 50);
});

// Add a fun hover effect to navigation links
const navLinks = document.querySelectorAll("nav a");
navLinks.forEach((link) => {
  link.addEventListener("mouseover", () => {
    link.style.color = "#ff6347"; // Change color to tomato
    link.style.transform = "scale(1.1)"; // Slightly enlarge the link
    link.style.transition = "all 0.3s ease";
  });

  link.addEventListener("mouseout", () => {
    link.style.color = "#fff"; // Revert to original color
    link.style.transform = "scale(1)"; // Revert to original size
  });
});

// Add a random fun fact generator
const funFacts = [
  "Did you know? KeyFix tools are compatible with over 99% of laptops worldwide!",
  "Fun Fact: The average person types 40 words per minute. With KeyFix, you can type even faster!",
  "KeyFix was inspired by a sticky keyboard incident during a hackathon!",
  "Our team once unstuck 500 keys in a single day using KeyFix tools!",
  "KeyFix Deluxe comes with a lifetime warranty. That's how confident we are!"
];

const funFactButton = document.createElement("button");
funFactButton.textContent = "Click for a Fun Fact!";
funFactButton.style.marginTop = "20px";
funFactButton.style.padding = "10px 20px";
funFactButton.style.backgroundColor = "#333";
funFactButton.style.color = "#fff";
funFactButton.style.border = "none";
funFactButton.style.borderRadius = "5px";
funFactButton.style.cursor = "pointer";
funFactButton.style.transition = "all 0.3s ease";

funFactButton.addEventListener("mouseover", () => {
  funFactButton.style.backgroundColor = "#ff6347"; // Change color to tomato
});

funFactButton.addEventListener("mouseout", () => {
  funFactButton.style.backgroundColor = "#333"; // Revert to original color
});

funFactButton.addEventListener("click", () => {
  const randomFact = funFacts[Math.floor(Math.random() * funFacts.length)];
  alert(randomFact);
});

document.querySelector(".container").appendChild(funFactButton);
