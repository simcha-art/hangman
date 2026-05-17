import tkinter as tk
from tkinter import messagebox, simpledialog
from user_manager import UserManager

class WelcomeScreen:
    """Beautiful welcome screen with user selection and high scores"""
    
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.selected_user = None
    
    def show(self):
        """Show welcome screen and return selected username"""
        root = tk.Tk()
        root.title("🎮 Hangman Game - Welcome")
        root.geometry("600x700")
        root.configure(bg="#2c3e50")
        
        # Title
        title_label = tk.Label(
            root,
            text="🎮 HANGMAN GAME 🎮",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title_label.pack(pady=20)
        
        subtitle = tk.Label(
            root,
            text="ברוך הבאת!",
            font=("Arial", 14),
            bg="#2c3e50",
            fg="#3498db"
        )
        subtitle.pack(pady=5)
        
        # Username input frame
        input_frame = tk.Frame(root, bg="#2c3e50")
        input_frame.pack(pady=20)
        
        username_label = tk.Label(
            input_frame,
            text="שם משתמש:",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        username_label.pack(side=tk.LEFT, padx=5)
        
        self.username_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=20,
            bg="#34495e",
            fg="#ecf0f1"
        )
        self.username_entry.pack(side=tk.LEFT, padx=5)
        
        # Buttons frame
        button_frame = tk.Frame(root, bg="#2c3e50")
        button_frame.pack(pady=10)
        
        start_btn = tk.Button(
            button_frame,
            text="▶ התחל משחק",
            command=lambda: self.start_game(root),
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            padx=20,
            pady=10
        )
        start_btn.pack(side=tk.LEFT, padx=10)
        
        quit_btn = tk.Button(
            button_frame,
            text="✕ יציאה",
            command=root.quit,
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=10
        )
        quit_btn.pack(side=tk.LEFT, padx=10)
        
        # High scores frame
        scores_label = tk.Label(
            root,
            text="🏆 BEST PLAYERS 🏆",
            font=("Arial", 14, "bold"),
            bg="#2c3e50",
            fg="#f39c12"
        )
        scores_label.pack(pady=15)
        
        # High scores listbox
        scores_frame = tk.Frame(root, bg="#34495e")
        scores_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(scores_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.scores_listbox = tk.Listbox(
            scores_frame,
            font=("Arial", 10),
            bg="#34495e",
            fg="#ecf0f1",
            yscrollcommand=scrollbar.set,
            borderwidth=0
        )
        self.scores_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.scores_listbox.yview)
        
        self.display_high_scores()
        
        root.mainloop()
        return self.selected_user
    
    def start_game(self, root):
        """Start game with selected username"""
        username = self.username_entry.get().strip()
        
        if not username:
            messagebox.showerror("שגיאה", "אנא הכנס שם משתמש!")
            return
        
        if len(username) < 2 or len(username) > 20:
            messagebox.showerror("שגיאה", "שם משתמש חייב להיות בין 2 ל-20 תווים")
            return
        
        # Check for invalid characters
        if not all(c.isalnum() or c == '_' or c == '-' for c in username):
            messagebox.showerror("שגיאה", "שם משתמש יכול להכיל אותיות, מספרים, _, -")
            return
        
        # Create or get user
        self.user_manager.create_user(username)
        self.selected_user = username
        root.quit()
    
    def display_high_scores(self):
        """Display high scores in listbox"""
        self.scores_listbox.delete(0, tk.END)
        high_scores = self.user_manager.get_high_scores(5)
        
        if not high_scores:
            self.scores_listbox.insert(tk.END, "אין נתונים עדיין...")
            return
        
        self.scores_listbox.insert(tk.END, "")
        for i, player in enumerate(high_scores, 1):
            score_text = f"{i}. {player['username']} - {player['games_won']}/{player['games_played']} ניצחונות"
            self.scores_listbox.insert(tk.END, score_text)
            best_text = f"   שיא: {player['best_wrong']} ניחושים שגויים"
            self.scores_listbox.insert(tk.END, best_text)
        self.scores_listbox.insert(tk.END, "")
