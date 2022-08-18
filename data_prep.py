from numpy import NaN
from pandas import concat
from soupsieve import select
from getters import *
from understat import *
from mergers import *
from cleaners import *

import match_names as mn

def get_dataset():
    # dataset consisting of performances of epl players
    # in every game recorded on understat
    epl_players = get_epl_data()[1]
    epl_players = pd.DataFrame(epl_players)

    dataset = pd.DataFrame([])

    for player in epl_players.head(3).iterrows():
        #player.to_csv('example.csv')
        player = player[1]
        print('player', player)
        id = player['id']
        print('ID ', id)
        player_data = get_player_data(id)
        player_data = pd.DataFrame(player_data[0])
        dataset = pd.concat([dataset, player_data])

    return dataset


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
    df.loc[df['was_home'] == True, 'a_team'] = NaN
    return df

def add_home_team_column(df):
    df['h_team'] = df['opp_team_name']
    df.loc[df['was_home'] == True, 'a_team'] = NaN
    return df

def transform_season_column(df):
    df = df.rename(columns = {'season_x': 'season'})
    df['season'] = df['season'].str[:-3]
    return df


def exclude_columns(df, excluded_columns):
    df = df.loc[:, ~df.columns.isin(excluded_columns)]
    return df


def add_rolling_columns(df, rolling_columns):
    for c in rolling_columns:
        df[c + '_avg5'] = df[c].rolling(5, min_periods=1).mean()
    return df


def merged_understat_and_fpl(rolling_columns = [], save_to_file = False):

    epl_players = get_epl_data()[1]
    epl_players = pd.DataFrame(epl_players)

    fpl_data = pd.read_csv('fpl_players.csv')
    fpl_data = transform_season_column(fpl_data)
    print('HMS', fpl_data[fpl_data['name'] == 'Heung-Min Son'])

    # add h_team, a_team columns to fpl_player
    print('LEN WAS HOME', len(fpl_data[fpl_data['was_home'] == True]))
    print('LEN WAS NOT HOME', len(fpl_data[fpl_data['was_home'] == False]))
    
    fpl_data = add_away_team_column(fpl_data)

    fpl_data = add_home_team_column(fpl_data)
    # print('fpl_data:', fpl_data['h_team'])

    dataset = pd.DataFrame([])
    for player in epl_players.head(100).iterrows():
        player = player[1]
        # get understat data for this player
        id = get_player_id(player)
        #print('ID ', id)
        #print(player)
        
        understat_player = pd.DataFrame(get_player_data(id)[0])

        # add name columns
        understat_player['player_name'] = player['player_name']

        # find fpl name
        fpl_name = find_fpl_name(player)

        # get fpl data for this player
        fpl_player = fpl_data.loc[fpl_data['name'] == fpl_name]

        # print('LEN U FPL', len(understat_player), len(fpl_player))

        # join the rows on name, season, a_team, h_team
        # part on a_team, part on h_team
        
        # pd.concat([fpl_player, understat_player], on=['season', 'h_team'], join='left')

        # print('fpl_player: ', fpl_player)
        # print('fpl_player keys: ', len(fpl_player.columns))
        # print('understat_player: ', understat_player)
        # print('understat_player keys: ', len(understat_player.columns))

        # fpl joined with understat
        merged_a_team = pd.merge(fpl_player, understat_player, left_on=['season', 'a_team'], right_on=['season', 'a_team'], how='inner', suffixes=['_fpl', '_und'])
        merged_h_team = pd.merge(fpl_player, understat_player, left_on=['season', 'h_team'], right_on=['season', 'h_team'], how='inner', suffixes=['_fpl', '_und'])
        
        if (len(merged_a_team) == 0 and len(merged_h_team) == 0 ):
            print(player['id'])
            print('Name', player['player_name'])

        merged = pd.concat([merged_a_team, merged_h_team])
        # print('LEN A H', len(merged_a_team), len(merged_h_team), len(merged))

        # adding rolling columns
        merged = add_rolling_columns(merged, rolling_columns)

        # fpl_player.join()
        # print('EVERTON FPL', fpl_player[ (fpl_player['season'] == '2020') & (fpl_player['a_team'] == 'Everton') ])

        # print('merged_player: ', merged)
        # print('merged_player keys: ', len(merged.columns))

        # print('first row', fpl_player.iloc[0])
        # merged rows with current dataset
        dataset = pd.concat([dataset, merged])

    excluded_columns = ['h_team_und', 'a_team_und', 'h_team_fpl', 'a_team_fpl', 'roster_id']
    dataset = exclude_columns(dataset, excluded_columns)

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