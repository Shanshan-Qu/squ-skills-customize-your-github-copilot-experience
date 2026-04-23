# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman word-guessing game using Python strings, loops, and user input, practising string manipulation, conditionals, and random selection.

## 📝 Tasks

### 🛠️	Set Up the Word and Guess Tracking

#### Description
Create the core data structures for the game: randomly select a hidden word and track which letters have been guessed.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list using the `random` module
- Represent the hidden word as blanks (`_ _ _` format), revealing correct guesses
- Track the set of letters the player has already guessed
- Track the number of incorrect guesses remaining


### 🛠️	Build the Game Loop

#### Description
Implement the interactive game loop that accepts player input, updates the game state, and determines the outcome.

#### Requirements
Completed program should:

- Prompt the player to guess a letter each turn
- Update the displayed word when a correct letter is guessed
- Decrement remaining attempts for each incorrect guess
- End the game when the word is fully guessed or attempts are exhausted
- Display a win or lose message at the end of the game

