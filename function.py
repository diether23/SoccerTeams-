

lstTeamNames = ["Az,CO,BYU,UTAH"]
#cordelia 

#this lst needs to be inculded in the main code along with calling the function we can cnhange or add teams as needed 
lstTeamNames = ["UVU",
  "Utah State",
  "UNLV",
  "TCU"]

def choose_team(teams,removed_team=None) :
    print("Here is the list of teams to choose from")
    for teams in lstTeamNames:
        print(teams)
    print(" ")
    team = input("Pick a team: ").strip()
    if team in lstTeamNames: 
        lstTeamNames.remove(team)
    else :
     return     # Remove that team from the list. 
    if removed_team is not None and removed_team in teams: 
        teams = [team for team in teams if team != {removed_team}]
    #Display list of all teams and allow the user to choose a team using a menu. 
    for i, team in enumerate(teams, 1):
        print(f"{i}. {team}")
    ichoice = int(input("Pick the corresponding number for the team: "))
    return teams[ichoice - 1]
        


#this is how we need to call this function in the main code 
home_team = choose_team(lstTeamNames)
# Call the function again to let the user choose the opponent but do not display the team they chose previously. 
away_team = choose_team(lstTeamNames, home_team)