class HangmanGame:
    """Core logic for Hangman game"""
    
    def __init__(self, word):
        self.word = word.lower()
        self.guessed_letters = set()
        self.wrong_guesses = set()
        self.max_wrong = 6
        self.game_over = False
        self.won = False
    
    def guess_letter(self, letter):
        """Process a letter guess"""
        letter = letter.lower()
        
        # Validate input
        if not letter.isalpha() or len(letter) != 1:
            return False, "הזן אות אחת בלבד (אנגלית)"
        
        if letter in self.guessed_letters or letter in self.wrong_guesses:
            return False, f"כבר ניחשת את האות '{letter}'"
        
        # Add to guessed letters
        self.guessed_letters.add(letter)
        
        # Check if correct
        if letter in self.word:
            # Check if won
            if self.is_won():
                self.game_over = True
                self.won = True
            return True, "נכון! ✓"
        else:
            self.wrong_guesses.add(letter)
            if len(self.wrong_guesses) >= self.max_wrong:
                self.game_over = True
                self.won = False
            return False, "טעיתה! ✗"
    
    def get_display_word(self):
        """Get word with blanks for guessed letters"""
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()
    
    def is_won(self):
        """Check if player won"""
        return all(letter in self.guessed_letters for letter in self.word)
    
    def get_wrong_count(self):
        """Get number of wrong guesses"""
        return len(self.wrong_guesses)
    
    def get_remaining_attempts(self):
        """Get remaining attempts"""
        return self.max_wrong - len(self.wrong_guesses)
    
    def get_hangman_stage(self):
        """Get ASCII hangman for current stage (building up from empty)"""
        stages = [
            # Stage 0: Empty gallows
            """
               --------
               |      |
               |
               |
               |
               |
               -
            """,
            # Stage 1: Head
            """
               --------
               |      |
               |      O
               |
               |
               |
               -
            """,
            # Stage 2: Body
            """
               --------
               |      |
               |      O
               |      |
               |
               |
               -
            """,
            # Stage 3: Left arm
            """
               --------
               |      |
               |      O
               |     \\|
               |
               |
               -
            """,
            # Stage 4: Right arm
            """
               --------
               |      |
               |      O
               |     \\|/
               |
               |
               -
            """,
            # Stage 5: Left leg
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     /
               -
            """,
            # Stage 6: Right leg (complete hangman)
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """
        ]
        return stages[min(len(self.wrong_guesses), len(stages) - 1)]
    
    def get_game_status(self):
        """Get current game status"""
        return {
            'word': self.get_display_word(),
            'wrong_guesses': list(self.wrong_guesses),
            'guessed_letters': list(self.guessed_letters),
            'remaining': self.get_remaining_attempts(),
            'wrong_count': self.get_wrong_count(),
            'game_over': self.game_over,
            'won': self.won,
            'actual_word': self.word if self.game_over else None
        }
