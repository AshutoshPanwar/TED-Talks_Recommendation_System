const inputField = document.getElementById("talk_content");

// Define an array of different placeholder texts
const placeholderTextOptions = [
	"Eg: Time Management and working hard to become successful in life.",
	"Eg: Climate change and impact on the health.",
	"Eg: Technology, Education, Motivation",
	"Eg: Climate Change, Artificial Intelligence, Art History",
];

let currentOptionIndex = 0; // Track current placeholder index

const typingSpeed = 120; // Adjust speed in milliseconds (higher for slower)

let animationIndex = 0;

function typingAnimation() {
	// Simulate typing by replacing characters in the placeholder
	inputField.placeholder = placeholderTextOptions[
		currentOptionIndex
	].substring(0, animationIndex + 1);
	animationIndex++;

	// Check if the entire placeholder has been typed
	if (animationIndex > placeholderTextOptions[currentOptionIndex].length) {
		animationIndex = 0; // Reset index for next placeholder
		currentOptionIndex++;

		// Wrap around to the first option if all options have been displayed
		if (currentOptionIndex >= placeholderTextOptions.length) {
			currentOptionIndex = 0;
		}
	}

	// Schedule the next animation frame with a delay for typing effect
	setTimeout(() => requestAnimationFrame(typingAnimation), typingSpeed);
}

// Start the animation when the page loads
window.addEventListener("load", typingAnimation);

// Stop the animation when the user focuses on the input field
inputField.addEventListener("focus", () => {
	clearTimeout(setTimeout(() => {}, 0)); // Clear any pending timeouts
	inputField.placeholder = placeholderTextOptions[currentOptionIndex]; // Set full placeholder
});
