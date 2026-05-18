import tkinter as tk
from tkinter import messagebox
import threading
import time

class GameOverScreen:
    """Beautiful game over screens for win and loss"""
    
    @staticmethod
    def show_win_screen(root, word, wrong_count):
        """Show celebration screen for winning"""
        root.destroy()
        
        win_window = tk.Tk()
        win_window.title("🎉 You Won! 🎉")
        win_window.geometry("600x500")
        win_window.configure(bg="#1abc9c")
        
        # Confetti animation
        confetti_label = tk.Label(
            win_window,
            text="🎉 🎊 🎈 🎁 ✨",
            font=("Arial", 40),
            bg="#1abc9c"
        )
        confetti_label.pack(pady=20)
        
        # Main message
        message = tk.Label(
            win_window,
            text="🏆 CONGRATULATIONS! 🏆",
            font=("Arial", 28, "bold"),
            bg="#1abc9c",
            fg="white"
        )
        message.pack(pady=20)
        
        # Word revealed
        word_label = tk.Label(
            win_window,
            text=f"The word was:",
            font=("Arial", 14),
            bg="#1abc9c",
            fg="white"
        )
        word_label.pack(pady=5)
        
        word_display = tk.Label(
            win_window,
            text=word.upper(),
            font=("Courier", 24, "bold"),
            bg="#27ae60",
            fg="white",
            padx=20,
            pady=10
        )
        word_display.pack(pady=10)
        
        # Stats
        stats_frame = tk.Frame(win_window, bg="#16a085")
        stats_frame.pack(fill=tk.X, padx=20, pady=20)
        
        wrong_text = tk.Label(
            stats_frame,
            text=f"Wrong Guesses: {wrong_count}",
            font=("Arial", 14, "bold"),
            bg="#16a085",
            fg="white"
        )
        wrong_text.pack(pady=10)
        
        # Close button
        close_btn = tk.Button(
            win_window,
            text="Continue",
            command=win_window.quit,
            font=("Arial", 14, "bold"),
            bg="#27ae60",
            fg="white",
            padx=30,
            pady=10
        )
        close_btn.pack(pady=20)
        
        win_window.mainloop()
    
    @staticmethod
    def show_lose_screen(root, word):
        """Show game over screen with hanging man for losing"""
        root.destroy()
        
        lose_window = tk.Tk()
        lose_window.title("💀 Game Over 💀")
        lose_window.geometry("600x700")
        lose_window.configure(bg="#2c3e50")
        
        # Title
        title = tk.Label(
            lose_window,
            text="💀 GAME OVER 💀",
            font=("Arial", 28, "bold"),
            bg="#2c3e50",
            fg="#e74c3c"
        )
        title.pack(pady=20)
        
        # Hangman frame
        hangman_frame = tk.Frame(lose_window, bg="#34495e")
        hangman_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        hangman_text = """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """
        
        hangman_label = tk.Label(
            hangman_frame,
            text=hangman_text,
            font=("Courier", 12),
            bg="#34495e",
            fg="#e74c3c",
            justify=tk.LEFT
        )
        hangman_label.pack(padx=20, pady=20)
        
        # Message
        message = tk.Label(
            lose_window,
            text="You ran out of attempts!",
            font=("Arial", 16),
            bg="#2c3e50",
            fg="#e74c3c"
        )
        message.pack(pady=10)
        
        # Word reveal
        word_label = tk.Label(
            lose_window,
            text="The word was:",
            font=("Arial", 14),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        word_label.pack(pady=5)
        
        word_display = tk.Label(
            lose_window,
            text=word.upper(),
            font=("Courier", 24, "bold"),
            bg="#c0392b",
            fg="white",
            padx=20,
            pady=10
        )
        word_display.pack(pady=10)
        
        # Close button
        close_btn = tk.Button(
            lose_window,
            text="Try Again",
            command=lose_window.quit,
            font=("Arial", 14, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=30,
            pady=10
        )
        close_btn.pack(pady=20)
        
        lose_window.mainloop()
