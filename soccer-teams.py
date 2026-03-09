# Group Project Members: Conner Major, Cade Sanders, Isaac Wood, Cordelia Diether

import random

# ---------------------------------------------------------
# Conner Major
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# Isaac Wood
# ---------------------------------------------------------
def display_menu():
    print("Menu: ")
    print("1. Play a season ")
    print("2. Exit ")
    choice = input("Enter your choice (1 or 2): ")
    return choice

# ---------------------------------------------------------
# Cordelia
# ---------------------------------------------------------
def choose_team(teams, removed_team=None):
    print("Here is the list of teams to choose from")
    if removed_team is not None and removed_team in teams: 
        # Fixed the set bracket syntax error here
        teams = [team for team in teams if team != removed_team]
    
    # Display list of all teams and allow the user to choose a team using a menu. 
    for i, team in enumerate(teams, 1):
        print(f"{i}. {team}")
    
    ichoice = int(input("Pick the corresponding number for the team: "))
    return teams[ichoice - 1]

# ---------------------------------------------------------
# Cade Sanders
# ---------------------------------------------------------
def gen_scores(home_team, opponent_list, number_games):
    # initialize list and dictionary to save info for printing later
    season_list = []
    season_record = {
        "Won Against": [],
        "Lost Against": []
    }

    # for each game in the season
    for game in range(0, number_games):

        away_team = choose_team(opponent_list, home_team) # this is to match the function created earlier

        # randomly generate scores. if it is tie, loop until it isnt
        home_score = random.randrange(0, 4)
        away_score = random.randrange(0, 4)
        while home_score == away_score:
            home_score = random.randrange(0, 4)
            away_score = random.randrange(0, 4)

        # save info depending on the home team winning or losing
        if home_score > away_score:
            season_list.append({
                "Game Number": game, 
                "Won Against": away_team,
                "Score": f"{home_score} - {away_score}"
            })
            season_record["Won Against"].append(away_team)
        else:
            season_list.append({
                "Game Number": game, 
                "Lost Against": away_team,
                "Score": f"{home_score} - {away_score}"
            })
            season_record["Lost Against"].append(away_team)

    return season_list, season_record

# ---------------------------------------------------------
# Main Function - Compiling everything
# ---------------------------------------------------------
def main():
    manager_name = display_intro()
    
    lstTeamNames = ["UVU", "Utah State", "UNLV", "TCU", "Az", "CO", "BYU", "UTAH"]
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            home_team = choose_team(lstTeamNames)
            
            num_games = int(input("How many games will you play? "))
            
            game_data, teams_list = gen_scores(home_team, lstTeamNames, num_games)
            
            print(f"\nFinal Record:")
            print(f"Wins: {len(teams_list['Won Against'])} Losses: {len(teams_list['Lost Against'])}\n")

            print(f"Teams won against:")
            for win in teams_list["Won Against"]:
                print(win, end = ' ')

            print(f"\n\nTeams lost against:")
            for loss in teams_list["Lost Against"]:
                print(loss, end = ' ')

            print(f"\n\nSeason information:")
            for game in game_data:
                if "Won Against" in game:
                    print(f"Game Number: {game['Game Number']}, Won Against: {game['Won Against']}, Score: {game['Score']}")
                else:
                    print(f"Game Number: {game['Game Number']}, Lost To: {game['Lost Against']}, Score: {game['Score']}")
            print("\n")
            
        elif choice == '2':
            break

if __name__ == "__main__":
    main()