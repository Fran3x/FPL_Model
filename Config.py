CURRENT_SEASON = "2023-24"
CURRENT_SEASON_FULL = "2023-2024"
NEXT_GAMEWEEK = 5

# training parameters
CUT_OFF_GAMEWEEK = 31
SEASON_TO_PREDICT = "2022-23"

# teams
current_teams = [
        'Arsenal',
        'Aston Villa',
        'Bournemouth',
        'Brentford',
        'Brighton',
        'Burnley',
        'Chelsea',
        'Crystal Palace',
        'Everton',
        'Fulham',
        'Liverpool',
        'Luton',
        'Manchester City',
        'Manchester Utd',
        'Newcastle Utd',
        "Nott'ham Forest",
        'Sheffield United',
        'Tottenham',
        'West Ham',
        'Wolves'
    ]

current_teams_fpl = [
        'Arsenal',
        'Aston Villa',
        'Bournemouth',
        'Brentford',
        'Brighton',
        'Burnley',
        'Chelsea',
        'Crystal Palace',
        'Everton',
        'Fulham',
        'Liverpool',
        'Luton',
        'Man City',
        'Man Utd',
        'Newcastle',
        "Nott'm Forest",
        'Sheffield Utd',
        'Spurs',
        'West Ham',
        'Wolves'
    ]


fbref_team_urls = [
        "https://fbref.com/en/squads/b8fd03ef/Manchester-City-Stats",
        "https://fbref.com/en/squads/7c21e445/West-Ham-United-Stats",
        "https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats",
        "https://fbref.com/en/squads/822bd0ba/Liverpool-Stats",
        "https://fbref.com/en/squads/18bb7c10/Arsenal-Stats",
        "https://fbref.com/en/squads/d07537b9/Brighton-and-Hove-Albion-Stats",
        "https://fbref.com/en/squads/8602292d/Aston-Villa-Stats",
        "https://fbref.com/en/squads/19538871/Manchester-United-Stats",
        "https://fbref.com/en/squads/cd051869/Brentford-Stats",
        "https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats",
        "https://fbref.com/en/squads/47c64c55/Crystal-Palace-Stats",
        "https://fbref.com/en/squads/fd962109/Fulham-Stats",
        "https://fbref.com/en/squads/b2b47a98/Newcastle-United-Stats",
        "https://fbref.com/en/squads/e4a775cb/Nottingham-Forest-Stats",
        "https://fbref.com/en/squads/8cec06e1/Wolverhampton-Wanderers-Stats",
        "https://fbref.com/en/squads/4ba7cbea/Bournemouth-Stats",
        "https://fbref.com/en/squads/1df6b87e/Sheffield-United-Stats",
        "https://fbref.com/en/squads/943e8050/Burnley-Stats",
        "https://fbref.com/en/squads/e297cd13/Luton-Town-Stats",
        "https://fbref.com/en/squads/d3fd31cc/Everton-Stats"
    ]

def current_teams_to_fpl(team):
    if team == "Manchester City":
        return 'Man City'
    if team == "Manchester Utd":
        return 'Man Utd'
    if team == "Newcastle Utd":
        return 'Newcastle'
    if team == "Nott'ham Forest":
        return "Nott'm Forest"
    if team == "Sheffield United":
        return 'Sheffield Utd'
    if team == "Tottenham":
        return 'Spurs'
    return team

# features
FEATURES_OUTFIELD = ['Was_home',
 'Rating_difference',
 'Price',
 'Transfers_balance',
 'Avg_FPL_points',
 'Min_2',
 'Gls_2',
 'Sh_2',
 'SoT_2',
 'Ast_2',
 'xG_2',
 'xA_2',
 'Team_CS_2',
 'Team_score_2',
 'Opp_score_2',
 'Team_result_2',
 'Player_GC_2',
 'FPL_points_2',
 'xP_2',
 'Min_4',
 'Gls_4',
 'Sh_4',
 'SoT_4',
 'Ast_4',
 'xG_4',
 'xA_4',
 'Team_CS_4',
 'Team_score_4',
 'Opp_score_4',
 'Team_result_4',
 'Player_GC_4',
 'FPL_points_4',
 'xP_4',
 'Min_30',
 'Gls_30',
 'Sh_30',
 'SoT_30',
 'Ast_30',
 'xG_30',
 'xA_30',
 'Team_CS_30',
 'Team_score_30',
 'Opp_score_30',
 'Team_result_30',
 'Player_GC_30',
 'FPL_points_30',
 'xP_30']


FEATURES_GK = ['Was_home',
 'Rating_difference',
 'Price',
 'Transfers_balance',
 'Avg_FPL_points',
 'Min_2',
 'Team_CS_2',
 'Player_GC_2',
 'Team_score_2',
 'Opp_score_2',
 'Team_result_2',
 'Saves_2',
 'FPL_points_2',
 'Min_4',
 'Team_CS_4',
 'Player_GC_4',
 'Team_score_4',
 'Opp_score_4',
 'Team_result_4',
 'Saves_4',
 'FPL_points_4',
 'Min_30',
 'Team_CS_30',
 'Player_GC_30',
 'Team_score_30',
 'Opp_score_30',
 'Team_result_30',
 'Saves_30',
 'FPL_points_30',
 'DEF',
 'FWD',
 'GK',
 'MID']