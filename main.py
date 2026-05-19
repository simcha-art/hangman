import random
from game_logic import HangmanGame
from ui import HangmanUI
from user_manager import UserManager
from start_screen import WelcomeScreen

def load_words(filename="words.txt"):
    """Load words from file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            words = [word.strip().lower() for word in f.readlines() if word.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return ["python", "hangman", "computer", "programming"]

def main():
    """Main game loop"""
    user_manager = UserManager()
    
    while True:
        # Welcome Screen
        welcome = WelcomeScreen(user_manager)
        current_user = welcome.show()
        
        if not current_user:
            break
        
        # Play game with same user until they quit
        while True:
            ui = HangmanUI(user_manager, current_user)
            ui.show()
            
            # User clicked menu, go back to player selection
            break

if __name__ == "__main__":
    main()
