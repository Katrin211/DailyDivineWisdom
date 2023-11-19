class User:
    def __init__(self, username):
        # Initialize a User object with a username
        self.username = username

    def display_message(self, message):
        # Display a formatted greeting along with the daily message
        print(f"\nHello, {self.username}!\nToday's Message: {message}")
