import json
import os
from datetime import datetime

class UserManager:
    """Manages user data and statistics stored in JSON"""
    
    def __init__(self, filename="users_data.json"):
        self.filename = filename
        self.users = self.load_users()
    
    def load_users(self):
        """Load users from JSON file, create if doesn't exist"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get('users', [])
            except:
                return []
        return []
    
    def save_users(self):
        """Save users to JSON file"""
        data = {'users': self.users}
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def user_exists(self, username):
        """Check if user exists"""
        return any(user['username'] == username for user in self.users)
    
    def create_user(self, username):
        """Create a new user profile"""
        if not self.user_exists(username):
            new_user = {
                'username': username,
                'games_played': 0,
                'games_won': 0,
                'total_wrong_guesses': 0,
                'best_wrong_guesses': float('inf'),
                'last_played': None
            }
            self.users.append(new_user)
            self.save_users()
            return new_user
        return self.get_user(username)
    
    def get_user(self, username):
        """Get user profile by username"""
        for user in self.users:
            if user['username'] == username:
                return user
        return None
    
    def update_game_stats(self, username, won, wrong_guesses):
        """Update user statistics after a game"""
        user = self.get_user(username)
        if user:
            user['games_played'] += 1
            if won:
                user['games_won'] += 1
            user['total_wrong_guesses'] += wrong_guesses
            if wrong_guesses < user['best_wrong_guesses']:
                user['best_wrong_guesses'] = wrong_guesses
            user['last_played'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.save_users()
    
    def get_high_scores(self, limit=5):
        """Get top players by win rate"""
        if not self.users:
            return []
        
        # Calculate win rate for each user
        scored_users = []
        for user in self.users:
            if user['games_played'] > 0:
                win_rate = user['games_won'] / user['games_played']
                avg_wrong = user['total_wrong_guesses'] / user['games_played']
                scored_users.append({
                    'username': user['username'],
                    'games_won': user['games_won'],
                    'games_played': user['games_played'],
                    'win_rate': win_rate,
                    'best_wrong': user['best_wrong_guesses'],
                    'avg_wrong': avg_wrong
                })
        
        # Sort by win rate, then by best wrong guesses
        scored_users.sort(key=lambda x: (-x['win_rate'], x['best_wrong']))
        return scored_users[:limit]
    
    def get_user_stats(self, username):
        """Get formatted stats for a user"""
        user = self.get_user(username)
        if not user:
            return None
        
        if user['games_played'] > 0:
            win_rate = (user['games_won'] / user['games_played']) * 100
            avg_wrong = user['total_wrong_guesses'] / user['games_played']
        else:
            win_rate = 0
            avg_wrong = 0
        
        return {
            'username': user['username'],
            'games_played': user['games_played'],
            'games_won': user['games_won'],
            'win_rate': f"{win_rate:.1f}%",
            'total_wrong': user['total_wrong_guesses'],
            'best_wrong': user['best_wrong_guesses'],
            'avg_wrong': f"{avg_wrong:.1f}",
            'last_played': user['last_played']
        }
