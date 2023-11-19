from messages import get_daily_message
from user import User


def main():
    # Welcome message and user input for username
    print("Welcome to the Spiritual Messages App!")
    username = input("Enter your username: ")

    # Create a User object
    user = User(username)

    # Main application loop
    while True:
        # Display menu options
        print("\n1. Get Daily Message")
        print("2. Exit")

        # User choice input
        choice = input("Enter your choice: ")

        # Perform actions based on user choice
        if choice == "1":
            message = get_daily_message()
            user.display_message(message)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
