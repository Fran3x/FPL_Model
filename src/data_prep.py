from numpy import NaN
from pandas import concat
from soupsieve import select
from vaastav.getters import *
from vaastav.understat import *
from vaastav.mergers import *
from vaastav.cleaners import *
from models.commons import *
from statistics import *

import numpy as np
from src import match_names as mn


def find_fpl_name(player):
    fpl_name = player['player_name']
    if player['player_name'] in mn.names:
        fpl_name = mn.names[player['player_name']]
    return fpl_name


def get_player_id(player):
    id = player['id']
    return id

def add_away_team_column(df):
    df['a_team'] = df['opp_team_name']
    df.loc[df['was_home'] == 0, 'a_team'] = NaN
    return df

def add_home_team_column(df):
    df['h_team'] = df['opp_team_name']
    df.loc[df['was_home'] == 1, 'h_team'] = NaN
    return df

def transform_season_column(df):
    df = df.rename(columns = {
        'season_x': 'season',
        'team_x': 'team'
    })
    df['season'] = df['season'].str[:-3]
    return df


def exclude_columns(df, excluded_columns):
    df = df.loc[:, ~df.columns.isin(excluded_columns)]
    return df


def add_rolling_columns(df, rolling_columns, gameweeks_for_averages):
    for gw_avg in gameweeks_for_averages:
        for c in rolling_columns:
            df[c + '_avg' + str(gw_avg)] = df[c].rolling(gw_avg, min_periods=1).mean()
    return df


def get_epl_players():
    epl_players = get_epl_data()[1]
    epl_players = pd.DataFrame(epl_players)
    return epl_players


def add_opp_team_for_current_season(dataset):
    teams = pd.read_csv('data/2022-23/teams.csv')
    
    # print(dataset.iloc[1])
    print('LENGTH', dataset[dataset['season'] == CURRENT_SEASON_UNDERSTAT].shape)
    
    for i, row in dataset[(dataset['season'] == CURRENT_SEASON_UNDERSTAT) | (dataset['season'] == CURRENT_SEASON_FPL)].iterrows():
        dataset.at[i, 'opp_team_name'] = teams[teams['id'] == row['opponent_team']].iloc[0]['name']

    return dataset


def add_missing_a_h_team(df):
    index = 0
    for i, row in df.iterrows():
        if row['was_home'] == 1:
            df.at[index, 'h_team'] = row['team']
        else:
            # print(df.iloc[0])
            df.at[index, 'a_team'] = row['team']
            
        index += 1
        
    return df


def get_fpl_data():
    fpl_data = pd.read_csv('fpl_players.csv')
    fpl_data = transform_season_column(fpl_data)

    # add h_team, a_team columns to fpl_player
    fpl_data = add_opp_team_for_current_season(fpl_data)
    fpl_data = add_away_team_column(fpl_data)
    fpl_data = add_home_team_column(fpl_data)
    fpl_data = add_missing_a_h_team(fpl_data)
    
    return fpl_data


def get_understand_player(player):
    # get understat data for this player
    id = get_player_id(player)
    
    understat_player = pd.DataFrame(get_player_data(id)[0])
    
    # add name columns
    understat_player['player_name'] = player['player_name']
    if len(understat_player) > 0 and understat_player.loc[0]['player_name'] == 'Mohamed Salah':
        print('SALAH')
        print(len(understat_player))
    
    return understat_player


def get_fpl_player(player, fpl_data):
    # find fpl name
    fpl_name = find_fpl_name(player)
    
    # get fpl data for this player
    fpl_player = fpl_data.loc[fpl_data['name'] == fpl_name]
    
    return fpl_player


def merge_player(player, merged_h_team, merged_a_team, rolling_columns, gameweeks_for_averages):
    if (len(merged_a_team) == 0 and len(merged_h_team) == 0 ):
        print(player['id'])
        print('Name', player['player_name'])
        
    
    if len(merged_h_team) > 0 and merged_h_team.iloc[0]['name'] == 'Mohamed Salah':
        print('SALAH')
        print(len(merged_h_team))
        print(len(merged_a_team))
        
    merged = pd.concat([merged_a_team, merged_h_team])
    
    # adding rolling columns
    merged = add_rolling_columns(merged, rolling_columns, gameweeks_for_averages)
    
    # indicating that game was played
    merged['was_played'] = 1
    merged['next_gw'] = 0
    
    return merged


def get_merged_a_team(fpl_player, understat_player, player_team):
    merged_a_team = fpl_player.merge(understat_player, on=['season', 'a_team'], suffixes=['_fpl', '_und'])
    merged_a_team = merged_a_team[merged_a_team['a_team'] != player_team]
    merged_a_team['h_team'] = player_team
    return merged_a_team

def get_merged_h_team(fpl_player, understat_player, player_team):
    merged_h_team = fpl_player.merge(understat_player, on=['season', 'h_team'], how='inner', suffixes=['_fpl', '_und'])
    merged_h_team = merged_h_team[merged_h_team['h_team'] != player_team]
    merged_h_team['a_team'] = player_team
    return merged_h_team


def load_player(player, fpl_data, rolling_columns, gameweeks_for_averages):
    # getting data from understat and fpl
    understat_player = get_understand_player(player)
    fpl_player = get_fpl_player(player, fpl_data)
    
    if player['player_name'] == 'Mohamed Salah':
        print(fpl_player)
        
    
    # no data found
    if len(understat_player) == 0 or len(fpl_player) == 0:
        return
    
    player_team = fpl_player.iloc[-1]['team']
    
    # fpl joined with understat
    merged_a_team = get_merged_a_team(fpl_player, understat_player, player_team)
    merged_h_team = get_merged_h_team(fpl_player, understat_player, player_team)
    
    # merging a_team with h_team
    merged_player = merge_player(player, merged_h_team, merged_a_team, rolling_columns, gameweeks_for_averages)
    
    return pd.DataFrame(merged_player)

    
def load_every_player(epl_players, fpl_data, rolling_columns, gameweeks_for_averages):
    # empty dataset
    dataset = pd.DataFrame([])
    
    for player in epl_players.head(100).iterrows():
        player = player[1]
        
        # merged rows with current dataset
        merged = load_player(player, fpl_data, rolling_columns, gameweeks_for_averages)
        
        # appending to dataset
        dataset = pd.concat([dataset, merged])
        
    # sorting by kickoff time
    dataset = dataset.sort_values(by='kickoff_time')
    return dataset


def clean_nans(df):
    df = df[df['h_team'].notna()]
    df = df[df['a_team'].notna()]
    return df


def add_opp_team(df):
    for i, row in df.iterrows():
        if row['was_home'] == 1:
            df.loc[i, 'opp_team'] = row['a_team']
        else:
            df.loc[i, 'opp_team'] = row['h_team']
    return df

    
def load_previous_games(rolling_columns, gameweeks_for_averages):
    epl_players = get_epl_players()
    fpl_data = get_fpl_data()
    
    dataset = load_every_player(epl_players, fpl_data, rolling_columns, gameweeks_for_averages)

    excluded_columns = ['h_team_und', 'a_team_und', 'h_team_fpl', 'a_team_fpl', 'roster_id']
    dataset = exclude_columns(dataset, excluded_columns)
    dataset['was_home'] = dataset['was_home'].astype(int)
    
    dataset = dataset.dropna(subset = ['team'])
    dataset = add_opp_team(dataset)
    
    # team ratings
    dataset = add_team_rating(dataset)
    dataset = add_opposite_team_rating(dataset)
    dataset = add_team_rating_diff(dataset)
    
    # dataset = clean_nans(dataset)
    
    return dataset


def get_fixtures_for_next_gw(fixtures, gameweek):
    result = []
    for fixture in fixtures:
        if fixture['event'] == gameweek:
            result.append(fixture)
            
    return result

def get_fixtures_for_next_gw_by_id(fixtures, gameweek, team_id):
    fixtures_next_gw = []
    for fixture in fixtures:
        if fixture['event'] == gameweek:
            fixtures_next_gw.append(fixture)
            
    fixtures_next_gw = pd.DataFrame(fixtures_next_gw)
    # print(fixtures_next_gw)
    result = fixtures_next_gw[fixtures_next_gw['team_h'] == team_id]
    if len (result) <= 0:
        result = fixtures_next_gw[fixtures_next_gw['team_a'] == team_id]
    
    return result


def get_team_for_current_season():
    teams = pd.read_csv('data/2022-23/teams.csv')
    
    return teams


def get_team_by_id(team_id):
    teams = pd.read_csv('data/2022-23/teams.csv')
    
    team = teams[teams['id'] == team_id].iloc[0]
    
    return team['name']


def get_team_name_for_rating(team_name):
    if team_name == "Nott'm Forest":
        return 'Forest'
    elif team_name == "Man Utd":
        return 'Man United'
    elif team_name == "Spurs":
        return 'Tottenham'
    return team_name


def get_rating_for_team(team_ratings, team_name, date):
    team_name = get_team_name_for_rating(team_name)
    # print('INFO RATING', team_name)
    previous_rating = team_ratings[(team_ratings['From'] <= date.strftime("%Y-%m-%d")) & (team_ratings['Club'] == team_name)]
    last_rating = previous_rating.iloc[-1]
    rating_value = last_rating['Elo']
    return rating_value


def get_teams_names():
    result = []
    teams = pd.read_csv('data/2022-23/teams.csv')
    for t in teams.iterrows():
        if t[1]['name'].replace(" ", "") == "Nott'mForest":
            result.append('Forest')
        elif t[1]['name'].replace(" ", "") == "ManUtd":
            result.append('ManUnited')
        elif t[1]['name'].replace(" ", "") == "Spurs":
            result.append('Tottenham')
        else:
            result.append(t[1]['name'].replace(" ", ""))
    return result


def reload_all_teams_ratings():
    result = pd.DataFrame()
    for team in get_teams_names():
        response = get_data('http://api.clubelo.com/' + team)
        print(team, len(response))
        rows = response.splitlines()
        columns = rows[0].split(',')
        content = []
        for r in rows[1:]:
            content.append(r.split(','))
        df = pd.DataFrame(content, columns = columns)
        result = pd.concat([result, df])
    result = result.dropna()
    result.to_csv('team_ratings_history.csv')
    
    
def load_all_teams_ratings():
    df = pd.read_csv('team_ratings_history.csv')
    return df


def add_team_rating(df):
    team_ratings = load_all_teams_ratings()
    
    for i, row in df.iterrows():
        # print('row', row)
        # print('team', row['team'])
        df.loc[i, 'team_rating'] = get_rating_for_team(team_ratings, row['team'], NEXT_GAMEWEEK_DATE)
    return df


def add_opposite_team_rating(df):
    team_ratings = load_all_teams_ratings()
    
    for i, row in df.iterrows():
        df.loc[i, 'opp_team_rating'] = get_rating_for_team(team_ratings, row['opp_team'], NEXT_GAMEWEEK_DATE)
    return df


def add_team_rating_diff(df):
    df['rating_diff'] = ( df['team_rating'] - df['opp_team_rating'] ) / df['opp_team_rating']
    return df


def add_team_rating_columns(df):    
    df = add_team_rating(df)
    df = add_opposite_team_rating(df)
    df = add_team_rating_diff(df)
    return df


def add_columns_for_next_fixture(player_next_fixture, player):
    player_next_fixture['name'] = player['player_name']
    player_next_fixture['team_h'] = get_team_by_id(player_next_fixture['team_h'].iloc[0])
    player_next_fixture['team_a'] = get_team_by_id(player_next_fixture['team_a'].iloc[0])
    player_next_fixture['team'] = player['team']
    return player_next_fixture

def add_home_and_opp_team(player_next_fixture, player):
    if player['team'] == player_next_fixture['team_h'].iloc[0]:
        player_next_fixture['was_home'] = 1
        player_next_fixture['opp_team'] = player_next_fixture['team_a']
    else:
        player_next_fixture['was_home'] = 0
        player_next_fixture['opp_team'] = player_next_fixture['team_h']
    return player_next_fixture


def get_next_gameweek(df, gameweek_nr, rolling_columns, gameweeks_for_averages):
    # dropping rows before transfers to their current teams
    df_unique_players = df[['player_name', 'team']].drop_duplicates(subset=['player_name'], keep='last')
    df_unique_players = pd.DataFrame(df_unique_players.dropna())
    
    # print(df_unique_players[df_unique_players['player_name'] == 'Ben Mee'])
    
    teams = get_team_for_current_season()
    fixtures = get_fixtures_data()
    
    # empty next gameweek
    next_gameweek = pd.DataFrame()
    
    # getting a game for every player
    for player in df_unique_players.iterrows():
        player = player[1]
        # print('PLAYER', player)
        # print('PLAYER TEAM', player['team'])
        team = teams[teams['name'] == player['team']]
        # print('TEAM', team)
        team_id = int(team['id'])
        
        # last fixture for a player
        last_fixture = df[df['player_name'] == player['player_name']].iloc[-1]
        
        next_fixture = get_fixtures_for_next_gw_by_id(fixtures, NEXT_GAMEWEEK, team_id)

        player_next_fixture = pd.DataFrame(next_fixture[['event', 'kickoff_time', 'team_a', 'team_h']])
        
        player_next_fixture = add_columns_for_next_fixture(player_next_fixture, player)
        player_next_fixture = add_home_and_opp_team(player_next_fixture, player)
        
        player_next_fixture['position_fpl'] = last_fixture['position_fpl']
        
        next_gameweek = pd.concat([next_gameweek, player_next_fixture])

    
    next_gameweek = next_gameweek.reset_index()
    next_gameweek = next_gameweek.drop(columns='index')
    next_gameweek = next_gameweek.sort_values(by='kickoff_time')
    next_gameweek['next_gameweek'] = True
    
    # renaming columns
    next_gameweek = next_gameweek.rename(columns = {'team_h': 'h_team', 'team_a': 'a_team', 'event': 'fixture'})
    
    df['next_gameweek'] = False
    next_gameweek = add_rolling_columns_for_next_gw(pd.concat([df, next_gameweek]), rolling_columns, gameweeks_for_averages)
    
    next_gameweek = next_gameweek[next_gameweek['next_gameweek'] == True]
    
    next_gameweek['was_home'] = next_gameweek['was_home'].astype(int)
    
    # team ratings
    next_gameweek = add_team_rating_columns(next_gameweek)
    
    return next_gameweek


def add_rolling_columns_for_next_gw(df, rolling_columns, gameweeks_for_averages):
    for i, row in df.iterrows():
        if row['next_gameweek'] == True:
            player_name = row['name']
            for gw_avg in gameweeks_for_averages:
                for c in rolling_columns:
                    df.loc[i, c + '_avg' + str(gw_avg)] = mean([float(i) for i in np.array(df[df['name'] == player_name].tail(gw_avg + 1).head(gw_avg)[c])])
    return df
    
    
def merged_understat_and_fpl(rolling_columns = [], gameweeks_for_averages = [], save_to_file = False):
    # returns all previous performances
    dataset = load_previous_games(rolling_columns, gameweeks_for_averages)

    # saving to file
    if save_to_file:
        dataset.to_csv('merged_dataset.csv')

    return dataset


def load_dataset():
    df = pd.read_csv('merged_dataset.csv')
    return df


if __name__ == "__main__":
    dataset = merged_understat_and_fpl([], False)

    print('columns', dataset.columns)
    dataset.to_csv('merged_dataset.csv')