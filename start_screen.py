import tkinter as tk
from tkinter import simpledialog, messagebox

class WelcomeScreen:
    """Welcome screen with user selection and beautiful leaderboard"""
    
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.root = None
        self.selected_user = None
    
    def show(self):
        """Display the welcome screen"""
        self.root = tk.Tk()
        self.root.title("🎮 Hangman Game - Welcome")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a252f")
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#1a252f")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🎮 HANGMAN GAME",
            font=("Arial", 32, "bold"),
            bg="#1a252f",
            fg="#3498db"
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Welcome! Select a player or create a new one",
            font=("Arial", 12),
            bg="#1a252f",
            fg="#ecf0f1"
        )
        subtitle_label.pack(pady=10)
        
        # Button frame for controls
        control_frame = tk.Frame(main_frame, bg="#1a252f")
        control_frame.pack(pady=20)
        
        tk.Button(
            control_frame,
            text="➕ New Player",
            command=self.new_player,
            font=("Arial", 12, "bold"),
            bg="#2ecc71",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            control_frame,
            text="❌ Quit",
            command=self.quit_game,
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=10)
        
        # Players section
        players_label = tk.Label(
            main_frame,
            text="📊 PLAYERS & LEADERBOARD",
            font=("Arial", 14, "bold"),
            bg="#1a252f",
            fg="#f39c12"
        )
        players_label.pack(pady=15)
        
        # Scrollable frame for player cards
        canvas_frame = tk.Frame(main_frame, bg="#1a252f")
        canvas_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        canvas = tk.Canvas(canvas_frame, bg="#1a252f", highlightthickness=0)
        scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#1a252f")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Display player cards
        high_scores = self.user_manager.get_high_scores(limit=10)
        
        if high_scores:
            for idx, player in enumerate(high_scores, 1):
                self.create_player_card(scrollable_frame, idx, player)
        else:
            no_players_label = tk.Label(
                scrollable_frame,
                text="No players yet. Create a new player to start!",
                font=("Arial", 12),
                bg="#1a252f",
                fg="#95a5a6"
            )
            no_players_label.pack(pady=20)
        
        # All users section (clickable)
        all_users_label = tk.Label(
            main_frame,
            text="👥 ALL PLAYERS",
            font=("Arial", 14, "bold"),
            bg="#1a252f",
            fg="#9b59b6"
        )
        all_users_label.pack(pady=15)
        
        # Frame for all users buttons
        all_users_frame = tk.Frame(main_frame, bg="#1a252f")
        all_users_frame.pack(fill=tk.X, pady=10)
        
        users = self.user_manager.users
        if users:
            for user in users:
                self.create_user_button(all_users_frame, user['username'])
        else:
            no_users_label = tk.Label(
                all_users_frame,
                text="No players created yet",
                font=("Arial", 11),
                bg="#1a252f",
                fg="#95a5a6"
            )
            no_users_label.pack()
        
        self.root.mainloop()
        return self.selected_user
    
    def create_player_card(self, parent, rank, player):
        """Create a beautiful player card"""
        card_frame = tk.Frame(
            parent,
            bg="#2c3e50",
            highlightbackground="#3498db",
            highlightthickness=2,
            height=100
        )
        card_frame.pack(fill=tk.X, pady=10, padx=5)
        
        # Left side - rank and name
        left_frame = tk.Frame(card_frame, bg="#34495e")
        left_frame.pack(side=tk.LEFT, padx=15, pady=10)
        
        rank_label = tk.Label(
            left_frame,
            text=f"#{rank}",
            font=("Arial", 20, "bold"),
            bg="#34495e",
            fg="#f39c12"
        )
        rank_label.pack()
        
        name_label = tk.Label(
            left_frame,
            text=player['username'],
            font=("Arial", 14, "bold"),
            bg="#34495e",
            fg="#ecf0f1"
        )
        name_label.pack()
        
        # Right side - stats in columns
        right_frame = tk.Frame(card_frame, bg="#2c3e50")
        right_frame.pack(side=tk.RIGHT, padx=20, pady=10, fill=tk.X, expand=True)
        
        # Win rate
        win_rate_frame = tk.Frame(right_frame, bg="#2c3e50")
        win_rate_frame.pack(side=tk.LEFT, padx=15)
        
        tk.Label(
            win_rate_frame,
            text="🏆 Win Rate",
            font=("Arial", 10, "bold"),
            bg="#2c3e50",
            fg="#95a5a6"
        ).pack()
        
        tk.Label(
            win_rate_frame,
            text=f"{player['win_rate']*100:.1f}%",
            font=("Arial", 14, "bold"),
            bg="#2c3e50",
            fg="#2ecc71"
        ).pack()
        
        # Games won
        won_frame = tk.Frame(right_frame, bg="#2c3e50")
        won_frame.pack(side=tk.LEFT, padx=15)
        
        tk.Label(
            won_frame,
            text="✅ Wins",
            font=("Arial", 10, "bold"),
            bg="#2c3e50",
            fg="#95a5a6"
        ).pack()
        
        tk.Label(
            won_frame,
            text=f"{player['games_won']}",
            font=("Arial", 14, "bold"),
            bg="#2c3e50",
            fg="#3498db"
        ).pack()
        
        # Total games
        games_frame = tk.Frame(right_frame, bg="#2c3e50")
        games_frame.pack(side=tk.LEFT, padx=15)
        
        tk.Label(
            games_frame,
            text="🎮 Games",
            font=("Arial", 10, "bold"),
            bg="#2c3e50",
            fg="#95a5a6"
        ).pack()
        
        tk.Label(
            games_frame,
            text=f"{player['games_played']}",
            font=("Arial", 14, "bold"),
            bg="#2c3e50",
            fg="#e74c3c"
        ).pack()
        
        # Best score
        best_frame = tk.Frame(right_frame, bg="#2c3e50")
        best_frame.pack(side=tk.LEFT, padx=15)
        
        tk.Label(
            best_frame,
            text="⭐ Best",
            font=("Arial", 10, "bold"),
            bg="#2c3e50",
            fg="#95a5a6"
        ).pack()
        
        best_score = player['best_wrong'] if player['best_wrong'] != float('inf') else "N/A"
        tk.Label(
            best_frame,
            text=f"{best_score}",
            font=("Arial", 14, "bold"),
            bg="#2c3e50",
            fg="#f39c12"
        ).pack()
    
    def create_user_button(self, parent, username):
        """Create a button for each user"""
        user_stats = self.user_manager.get_user_stats(username)
        
        # Mini card for user selection
        user_card = tk.Frame(
            parent,
            bg="#34495e",
            highlightbackground="#9b59b6",
            highlightthickness=1,
            height=80
        )
        user_card.pack(side=tk.LEFT, padx=8, pady=5, fill=tk.BOTH, expand=True)
        
        # Make it clickable
        def on_click():
            self.selected_user = username
            self.root.quit()
        
        for child in user_card.winfo_children():
            child.config(cursor="hand2")
        
        user_card.config(cursor="hand2")
        user_card.bind("<Button-1>", lambda e: on_click())
        
        # User name
        name_btn = tk.Label(
            user_card,
            text=username,
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="#3498db",
            cursor="hand2"
        )
        name_btn.pack(pady=8)
        name_btn.bind("<Button-1>", lambda e: on_click())
        
        # Stats line
        stats_text = f"🎮 {user_stats['games_played']} games | ✅ {user_stats['games_won']} wins"
        stats_label = tk.Label(
            user_card,
            text=stats_text,
            font=("Arial", 9),
            bg="#34495e",
            fg="#95a5a6",
            cursor="hand2"
        )
        stats_label.pack()
        stats_label.bind("<Button-1>", lambda e: on_click())
    
    def new_player(self):
        """Create a new player"""
        dialog = tk.Toplevel(self.root)
        dialog.title("New Player")
        dialog.geometry("300x150")
        dialog.configure(bg="#2c3e50")
        dialog.transient(self.root)
        dialog.grab_set()
        
        tk.Label(
            dialog,
            text="Enter your name:",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#ecf0f1"
        ).pack(pady=10)
        
        entry = tk.Entry(
            dialog,
            font=("Arial", 12),
            bg="#34495e",
            fg="#ecf0f1"
        )
        entry.pack(pady=10, padx=20, fill=tk.X)
        entry.focus()
        
        def create():
            username = entry.get().strip()
            if username:
                if self.user_manager.user_exists(username):
                    messagebox.showwarning("Exists", f"Player '{username}' already exists!")
                    return
                self.user_manager.create_user(username)
                self.selected_user = username
                dialog.destroy()
                self.root.quit()
            else:
                messagebox.showwarning("Empty", "Please enter a name!")
        
        tk.Button(
            dialog,
            text="Create",
            command=create,
            font=("Arial", 11, "bold"),
            bg="#2ecc71",
            fg="white",
            padx=20
        ).pack(pady=10)
        
        dialog.wait_window()
    
    def quit_game(self):
        """Quit the game"""
        self.selected_user = None
        self.root.quit()
