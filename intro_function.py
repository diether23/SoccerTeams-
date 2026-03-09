# Conner Major
# This is for our group Soccer Team project and this covers the first bullet point. I'll also be compiling everything together and getting it uploaded.

def display_intro():
    print("-" * 50)
    print("Welcome to the Women's Soccer Season Simulator!")
    print("-" * 50)
    print("Rules of the Game:")
    print("1. You will act as the team manager.")
    print("2. You will select a home team from a provided list.")
    print("3. For each game in the season, you will choose an opponent.")
    print("4. The system will simulate the games and generate random scores and you will either win or lose.")
    print("5. At the end, you'll see your team's complete season record.")
    print("-" * 50)
    
    # Prompt for the user's name
    manager_name = input("Please enter your name to begin: ")
    
    # Display the welcome message
    print(f"\nWelcome, Manager {manager_name}! Good luck!")
    print("-" * 50)
    
    # Return the name to be stored in a variable in the main program
    return manager_name