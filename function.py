

lstTeamNames = ["Az,CO,BYU,UTAH"]

def choose_team() :
    print("Here is the list of teams to choose from")
    for teams in lstTeamNames:
        print(teams)
    print(" ")
    team = input("Pick a team: ").strip()
    if team in lstTeamNames: 
        lstTeamNames.remove(team)
    else :
     return 