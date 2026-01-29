
# Higher Lower Game (Python CLI)

A simple Higher–Lower command-line game built with Python. The player compares two public figures or brands and guesses who has more followers. Each correct answer increases the score, and the game ends when the player makes a wrong guess.

---

## How the Game Works

1. The game randomly selects one entity as **A**
2. A different entity is selected as **B**
3. The player types `A` or `B` to guess who has more followers
4. If the answer is correct:
   - The score increases
   - The winning entity carries over to the next round
5. If the answer is wrong:
   - The game ends
   - The final score is displayed

---

## How to Run

### Requirements
- Python **3.8 or higher**
- No external libraries required

### Steps

1. Clone or download the repository  
2. Open a terminal / command prompt  
3. Navigate to the project folder

bash
cd higher-lower-game
python main.py

## Concepts Used
- Lists of dictionaries  
- Random number generation  
- Loops and conditional statements  
- Functions  
- Modular file imports  
- Command-line input/output  

---

## File Description

### main.py
- Controls the game flow  
- Handles user input  
- Manages score tracking  
- Performs follower comparison logic  

### gamedata.py
- Contains all comparison data  
- Stores names, follower counts, descriptions, and countries  

### art.py
- Stores ASCII art used for the game interface  

---

## Customization Ideas
- Add difficulty levels  
- Track high scores  
- Prevent repeated comparisons  
- Refactor into an object-oriented version  
- Add automated tests  

---

## License
This project is free to use for learning and personal purposes.

---

## Author
Built as a Python learning project with a focus on clean structure and readability.
