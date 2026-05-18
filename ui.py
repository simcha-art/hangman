import tkinter as tk
from tkinter import messagebox
import time
from game_logic import HangmanGame
from user_manager import UserManager

class HangmanUI:
    """TKINTER GUI for Hangman game with input validation"""
    
    def __init__(self, game, user_manager, username):
        self.game = game
        self.user_manager = user_manager
        self.username = username
        self.root = None
        self.letter_buttons = {}
        self.result_label = None
    
    def show(self):
        """Display the game window"""
        self.root = tk.Tk()
        self.root.title(f"🎮 Hangman Game - {self.username}")
        self.root.geometry("800x700")
        self.root.configure(bg="#2c3e50")
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title = tk.Label(
            main_frame,
            text=f"👋 Welcome, {self.username}!",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="#3498db"
        )
        title.pack(pady=10)
        
        # Hangman display
        hangman_frame = tk.Frame(main_frame, bg="#34495e")
        hangman_frame.pack(pady=10, fill=tk.BOTH)
        
        self.hangman_label = tk.Label(
            hangman_frame,
            text=self.game.get_hangman_stage(),
            font=("Courier", 10),
            bg="#34495e",
            fg="#ecf0f1",
            justify=tk.LEFT
        )
        self.hangman_label.pack(padx=10, pady=10)
        
        # Word display
        word_frame = tk.Frame(main_frame, bg="#2c3e50")
        word_frame.pack(pady=10)
        
        tk.Label(
            word_frame,
            text="Word:",
            font=("Arial", 12, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        ).pack(side=tk.LEFT, padx=5)
        
        self.word_label = tk.Label(
            word_frame,
            text=self.game.get_display_word(),
            font=("Courier", 14, "bold"),
            bg="#2c3e50",
            fg="#2ecc71"
        )
        self.word_label.pack(side=tk.LEFT, padx=5)
        
        # Stats frame
        stats_frame = tk.Frame(main_frame, bg="#34495e")
        stats_frame.pack(pady=10, fill=tk.X)
        
        tk.Label(
            stats_frame,
            text=f"Wrong Guesses: {self.game.get_wrong_count()}/6",
            font=("Arial", 11),
            bg="#34495e",
            fg="#e74c3c"
        ).pack(side=tk.LEFT, padx=20)
        
        tk.Label(
            stats_frame,
            text=f"Remaining: {self.game.get_remaining_attempts()}",
            font=("Arial", 11),
            bg="#34495e",
            fg="#f39c12"
        ).pack(side=tk.LEFT, padx=20)
        
        # Wrong guesses display
        wrong_frame = tk.Frame(main_frame, bg="#2c3e50")
        wrong_frame.pack(pady=10, fill=tk.X)
        
        tk.Label(
            wrong_frame,
            text="Wrong letters:",
            font=("Arial", 11, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        ).pack(side=tk.LEFT, padx=5)
        
        self.wrong_label = tk.Label(
            wrong_frame,
            text=", ".join(sorted(self.game.wrong_guesses)) or "None",
            font=("Arial", 11),
            bg="#2c3e50",
            fg="#e74c3c"
        )
        self.wrong_label.pack(side=tk.LEFT, padx=5)
        
        # Message label
        self.result_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#2ecc71"
        )
        self.result_label.pack(pady=5)
        
        # Alphabet buttons frame
        alphabet_frame = tk.Frame(main_frame, bg="#2c3e50")
        alphabet_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.create_alphabet_buttons(alphabet_frame)
        
        # Control buttons
        control_frame = tk.Frame(main_frame, bg="#2c3e50")
        control_frame.pack(pady=10)
        
        tk.Button(
            control_frame,
            text="🔄 New Game",
            command=self.new_game,
            font=("Arial", 11, "bold"),
            bg="#3498db",
            fg="white",
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            control_frame,
            text="✕ Quit",
            command=self.root.quit,
            font=("Arial", 11, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=15,
            pady=8
        ).pack(side=tk.LEFT, padx=5)
        
        self.root.mainloop()
    
    def create_alphabet_buttons(self, parent):
        """Create buttons for each letter"""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        button_frame = tk.Frame(parent, bg="#2c3e50")
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        for i, letter in enumerate(alphabet):
            row = i // 7
            col = i % 7
            
            btn = tk.Button(
                button_frame,
                text=letter.upper(),
                command=lambda l=letter: self.guess(l),
                font=("Arial", 10, "bold"),
                width=4,
                bg="#34495e",
                fg="#ecf0f1",
                activebackground="#3498db",
                padx=2,
                pady=2
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            self.letter_buttons[letter] = btn
        
        # Configure grid weights
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(7):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def guess(self, letter):
        """Process a letter guess"""
        if letter not in self.letter_buttons:
            return
        
        # Disable button
        self.letter_buttons[letter].config(state=tk.DISABLED, bg="#7f8c8d")
        
        # Process guess
        correct, message = self.game.guess_letter(letter)
        
        # Update display
        self.word_label.config(text=self.game.get_display_word())
        self.hangman_label.config(text=self.game.get_hangman_stage())
        self.wrong_label.config(text=", ".join(sorted(self.game.wrong_guesses)) or "None")
        
        # Update message
        color = "#2ecc71" if correct else "#e74c3c"
        self.result_label.config(text=message, fg=color)
        
        # Check game over
        if self.game.game_over:
            self.root.after(500, self.end_game)
    
    def end_game(self):
        """Handle game end"""
        # Disable all buttons
        for btn in self.letter_buttons.values():
            btn.config(state=tk.DISABLED)
        
        # Save stats
        self.user_manager.update_game_stats(
            self.username,
            self.game.won,
            self.game.get_wrong_count()
        )
        
        # Show result screen
        if self.game.won:
            self.show_win_screen()
        else:
            self.show_lose_screen()
    
    def show_win_screen(self):
        """Show beautiful win screen"""
        # Create new window
        win_window = tk.Toplevel(self.root)
        win_window.title("🎉 You Won!")
        win_window.geometry("500x500")
        win_window.configure(bg="#27ae60")
        win_window.grab_set()
        
        # Celebration text
        celebration = tk.Label(
            win_window,
            text="🎉 🎊 🎉",
            font=("Arial", 40, "bold"),
            bg="#27ae60",
            fg="#2ecc71"
        )
        celebration.pack(pady=20)
        
        # Win message
        win_text = tk.Label(
            win_window,
            text="CONGRATULATIONS!",
            font=("Arial", 28, "bold"),
            bg="#27ae60",
            fg="#ecf0f1"
        )
        win_text.pack(pady=10)
        
        # Word found
        word_text = tk.Label(
            win_window,
            text=f"The word was: {self.game.word.upper()}",
            font=("Arial", 18, "bold"),
            bg="#27ae60",
            fg="#f1c40f"
        )
        word_text.pack(pady=20)
        
        # Stats
        stats_text = tk.Label(
            win_window,
            text=f"Wrong Guesses: {self.game.get_wrong_count()}\nAttempts Used: {6 - self.game.get_remaining_attempts()}/6",
            font=("Arial", 14),
            bg="#27ae60",
            fg="#ecf0f1"
        )
        stats_text.pack(pady=20)
        
        # Buttons
        button_frame = tk.Frame(win_window, bg="#27ae60")
        button_frame.pack(pady=30)
        
        tk.Button(
            button_frame,
            text="🎮 Play Again",
            command=lambda: self.play_again(win_window),
            font=("Arial", 14, "bold"),
            bg="#2ecc71",
            fg="white",
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            button_frame,
            text="✕ Quit",
            command=self.root.quit,
            font=("Arial", 14, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=10)
    
    def show_lose_screen(self):
        """Show beautiful lose screen with hanging man"""
        # Create new window
        lose_window = tk.Toplevel(self.root)
        lose_window.title("💀 Game Over")
        lose_window.geometry("500x600")
        lose_window.configure(bg="#34495e")
        lose_window.grab_set()
        
        # Hangman display
        hangman_display = tk.Label(
            lose_window,
            text=self.game.get_hangman_stage(),
            font=("Courier", 12),
            bg="#34495e",
            fg="#e74c3c",
            justify=tk.LEFT
        )
        hangman_display.pack(pady=20)
        
        # Game over message
        game_over_text = tk.Label(
            lose_window,
            text="GAME OVER",
            font=("Arial", 28, "bold"),
            bg="#34495e",
            fg="#e74c3c"
        )
        game_over_text.pack(pady=10)
        
        # Word reveal
        word_text = tk.Label(
            lose_window,
            text=f"The word was: {self.game.word.upper()}",
            font=("Arial", 18, "bold"),
            bg="#34495e",
            fg="#f39c12"
        )
        word_text.pack(pady=20)
        
        # Stats
        stats_text = tk.Label(
            lose_window,
            text=f"Wrong Guesses: {self.game.get_wrong_count()}/6\nYou were close!",
            font=("Arial", 14),
            bg="#34495e",
            fg="#ecf0f1"
        )
        stats_text.pack(pady=20)
        
        # Buttons
        button_frame = tk.Frame(lose_window, bg="#34495e")
        button_frame.pack(pady=30)
        
        tk.Button(
            button_frame,
            text="🔄 Try Again",
            command=lambda: self.play_again(lose_window),
            font=("Arial", 14, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            button_frame,
            text="✕ Quit",
            command=self.root.quit,
            font=("Arial", 14, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=10)
    
    def play_again(self, window):
        """Start a new game"""
        window.destroy()
        self.root.quit()
    
    def new_game(self):
        """Start a new game"""
        self.root.quit()
