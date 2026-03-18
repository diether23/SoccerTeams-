
# Cade Sanders
# this code will be used to create a function that will generate scores for a team's season

import random


# function to randomly generate games to determine who wins or loses
# then stores that info to print later
# two inputs are the home team name and the number of games in the season
def gen_scores(home_team, opponent_list, number_games):

    # initialize list and dictionary to save info for printing later
    # you can probably just save them in season_list, but i think youd have to do
    # a more complicated loop when printing, so i would rather just have two storages
    season_list = []
    season_record = {
        "Won Against": [],
        "Lost Against": []
    }

    # for each game in the season
    for game in range(0, number_games):

        # let the user choose the away team for this loop
        # away_team = input(f"Enter the name of the away team for game {game}: ")

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

    # return the list and dictionary with the season info
    return season_list, season_record


# list to input into function
opponents_list = ["team1", "team2", "team3"]
# save the infos that the function return
game_data, teams_list = gen_scores('bananas', opponents_list, 3)

# print out the season info
# final record wins - losses
print(f"\nFinal Record:")
print(f"Wins: {len(teams_list["Won Against"])} Losses: {len(teams_list["Lost Against"])}\n")

# list the teams won against
print(f"Teams won against:")
for win in teams_list["Won Against"]:
    print(win, end = ' ')

# list the teams lost against
print(f"\n\nTeams lost against:")
for loss in teams_list["Lost Against"]:
    print(loss, end = ' ')

# print out the info for each game
print(f"\n\nSeason information:")
for game in game_data:
    if "Won Against" in game:
        print(f"Game Number: {game["Game Number"]}, Won Against: {game["Won Against"]}, Score: {game["Score"]}")
    else:
        print(f"Game Number: {game["Game Number"]}, Lost To: {game["Lost Against"]}, Score: {game["Score"]}")

