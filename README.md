# State-Capitals-Quiz-Game

This Python script is a simple quiz game that tests the user's knowledge of U.S. state capitals. The game randomly selects a U.S. state and asks the user to input the capital of that state. The program continues to ask the user for state capitals until they decide to quit by entering "q."

The game keeps track of both correct and incorrect answers. When the user decides to exit, the program displays the total number of correct and incorrect responses.

How the code works:
State-Capital Dictionary: The capitals dictionary stores all 50 U.S. states as keys and their respective capitals as values.
Random State Selection: Inside the while loop, a random state is chosen from the stateList (which is the list of all states).
User Input: The user is prompted to input the capital of the randomly selected state. If the user enters "q," the game exits.
Answer Checking: The user's answer is compared to the correct capital for the chosen state. If the answer matches (case-insensitive), the correct answer counter is incremented; otherwise, the incorrect answer counter increases.
Game Exit and Results: When the user quits, the total number of correct and incorrect answers is printed.
This script is a fun and interactive way to learn U.S. state capitals while practicing basic Python concepts like dictionaries, loops, user input, and conditional logic.
