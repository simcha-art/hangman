# 🎮 Hangman Game - Python Edition

A beautiful and interactive Hangman game built with Python and TKINTER, featuring user management, score tracking, and input validation.

## Features ✨

- 🎨 **Beautiful UI** - Clean and modern TKINTER interface
- 👤 **User Management** - Sign up and track multiple players
- 🏆 **High Scores** - Track your best performances in JSON database
- ✅ **Input Validation** - Only accepts valid English letters
- 📊 **Statistics** - Monitor games played, wins, and wrong guesses
- 🎯 **Hangman Stages** - Visual progression as you play

## Installation

```bash
git clone https://github.com/simcha-art/hangman.git
cd hangman
python main.py
```

## Requirements

- Python 3.x
- TKINTER (usually included with Python)

## Project Structure

```
hangman/
├── main.py              # Entry point
├── game_logic.py        # Game mechanics
├── start_screen.py      # Welcome screen & user selection
├── ui.py                # TKINTER GUI interface
├── user_manager.py      # User database & JSON handling
├── words.txt            # Word list for the game
├── users_data.json      # User profiles & statistics
└── README.md            # This file
```

## How to Play

1. **Start the Game** - Run `python main.py`
2. **Create/Select User** - Enter your username on the welcome screen
3. **Guess Letters** - Click buttons or type to guess letters
4. **Win or Lose** - Complete the word before running out of guesses
5. **Track Stats** - Your performance is automatically saved

## Game Rules

- Guess one letter at a time
- Only English letters (a-z) are allowed
- You have a limited number of wrong guesses
- Complete the word to win
- Each game is recorded in your profile

## Author

Created by simcha-art

## License

Open source - feel free to use and modify
