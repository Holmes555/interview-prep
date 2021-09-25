def tournamentWinner(competitions, results):
    teams = {}
    for i, t in enumerate(competitions):
        for team in t:
            if team not in teams:
                teams[team] = 0
        if results[i] == 0:
            teams[t[1]] += 3
        else:
            teams[t[0]] += 3
    return max(teams, key=teams.get)
