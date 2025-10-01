# Hangman Game

A classic command-line Hangman game written in Python. Guess the secret word letter by letter before you run out of tries! This version allows you to use your own custom word lists for endless fun.

---

## Gameplay Demo

```
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/
    by ori sela 2024

Do you want to open filemanager in GUI? [yes - Y] [no - N]:
Y
<-- A file dialog opens to select a word list -->

- - - - - - - - - - - - - - -
Enter a letter: a
Your letter is a
   x-------x
   |       |
   |       0
   |
   |
   |

p_t___-_r_g___
- - - - - - - - - - - - - - -
Enter a letter: e
You already guessed that letter
p_t___-_r_g___
```

---

## Features ✨

* **Custom Word Lists**: Use any `.txt` file as a source for words. Just put one word or phrase on each line.
* **GUI File Picker**: An easy-to-use graphical interface to select your word list file, in addition to a command-line path option.
* **ASCII Art**: The game visually displays the state of the hangman in the terminal.
* **"Play Again" Option**: After a win or a loss, you can immediately start a new game.
* **Switch Lists**: You can choose to play again with the same word list or select a new one for a different challenge.

---

## Requirements ⚙️

* **Python 3.x**
* **Tkinter library**: This is usually included with standard Python installations on Windows and macOS. If you are on a Debian-based Linux distribution (like Ubuntu), you may need to install it manually:
    ```bash
    sudo apt-get install python3-tk
    ```

---

## Setup & How to Run 🚀

### 1. File Structure

Place the game files in the same directory. You will also need to create your own word list file.

```
hangman_project/
├── game_logic.py   # The file containing the Game class
├── main.py         # The main script to run the game
└── words.txt       # An example word list file you create
```

### 2. Create a Word List

Create a file named `words.txt` (or any other name ending with `.txt`). Add words or phrases to it, with each one on a new line. The game automatically handles spaces by converting them to hyphens (`-`).

**Example `words.txt` content:**

```
python programming
visual studio code
artificial intelligence
open source
```

### 3. Run the Game

Open your terminal or command prompt, navigate to the `hangman_project` directory, and run the main script:

```bash
python main.py
```

---

## How to Play 🎮

1.  **Start the Game**: Run `main.py` from your terminal.
2.  **Select Word List**: You'll be asked if you want to use the GUI file manager.
    * Enter `Y` to open a window where you can browse and select your `.txt` file.
    * Enter `N` to type the file path directly into the terminal.
3.  **Guess a Letter**: The game will display the hidden word as underscores (`_`). Enter a single letter and press `Enter`.
4.  **Game Progress**:
    * If the letter is **correct**, it will be revealed in the word.
    * If the letter is **incorrect**, you will lose a try, and another part of the hangman will be drawn.
5.  **Win or Lose**:
    * You **win** by guessing all the letters in the word before running out of tries.
    * You **lose** if the full hangman is drawn.
6.  **Play Again**: After the game ends, you can choose to play another round with the same list or a new one.
