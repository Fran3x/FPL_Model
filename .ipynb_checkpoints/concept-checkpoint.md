Model predicting points:
- inputs:
  1. predicted xG
  2. predicted xA
  3. predicted CS
  4. predicted bps
- or:
  1. longer timeframe mean yellow cards
  2. longer timeframe mean red cards
  3. weighted average from last 100 days of xG, xA, BPS etc.
- one model for every position


Lineup evaluation model:
- projected points,
- flexibility:
  1. formation,
  2. popular price points,
  3. number of players from one club, e.g. 3xCity,
  4. funds spread over formations
  5. funds spread over players (e.g. 3xPremium)
- riskiness:
  1. average ownership,
  2. number of players from one club, e.g. 3xCity
  3. strength of the bench
  4. expected minutes of players


Features:
- Related to goal appetite:
    - 'goals_avg5'
    - 'xG_avg5'
    - 'shots_avg5'

- Related to creativity:
    - 'assists_fpl_avg5'
    
- Related to defensive capabilities:
    - 'clean_sheets_avg5'
    - 'goals_conceded_avg5'

- Related to general performance:
    - 'bonus_avg5', 
    - 'bps_avg5', 

- Related to team offensive form:
    - 'xGBuildup_avg5'
    - 'xGChain_avg5'
    
- Related to cards:
    - 'yellow_cards_avg5',
    - red_cards_avg5'
    
- Other:
    - 'was_home'
    


Feature ideas:
- team elo rating (percentage difference)




Player evaluation model:
- expected points,
- ownership,
- explosiveness,
- form,
- fixtures


Other ideas:
- calculating the biggest fixture swing
- one hot encoding for positions


Disclaimers:
Emerson appears twice in epl_players





How to update data:
- new data folder from /vaastav
- calling update.ipynb to merge previous_season with this_season and save it to fpl_players.csv
- merging fpl with understat using data_prep.py




Order:
- get new data from vaastav
- move cleaned_merged_seasons.csv to /data
- update.ipynb
- fbref_scrape.ipynb to get all fbref data
- merge_FPL_fbref.ipynb
- assign_team_to_df.ipynb
- LSTM_test.ipynb
- XGBoost_predictions.ipynb