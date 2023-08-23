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
- own metric focusing on correct order (Haaland > Salah)


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
    - 'red_cards_avg5'
    
- Other:
    - 'was_home'


Player evaluation model:
- expected points,
- ownership,
- explosiveness,
- form,
- fixtures


Other ideas:
- calculating the biggest fixture swing
- goalkeepers analysis (DF summary with shots conceded, xGC, xGC per shot, bonus points, etc.)
- upcoming/previous fixtures analysis


Data updating order:
- get new data from vaastav
- move cleaned_merged_seasons.csv to /data
- move master_team_list.csv from /vaastav to /data
- move data/current_season folder from /vaastav to /data
- FPL_players.ipynb
- fbref_scrape.ipynb to get all fbref data (~30 mins per season)
- merge_FPL_fbref.ipynb
- team_elo_rating.ipynb (to get newest elo ratings)
- assign_team_to_previous.ipynb (~9 mins)
- dataset_cleaning.csv (renaming columns etc.)
- LSTM_test.ipynb
- XGBoost_predictions.ipynb


File order:
- cleaned_merged_seasons.csv (from vaastav)
- fpl_players.csv (FPL)
- logs_all_PL.csv (fbRef)
- fpl_fbref_players.csv (2 previous files merged)
- final_dataset.csv (with team elo ratings)
- FPL_logs.csv (cleaned dataset)


Predictions file order:
- team_elo_rating.ipynb (to get newest elo ratings)
- active_players.ipynb (to track injuries)
- get_goalkeepers.ipynb (to get first choice goalkeepers)
- df_features_for_next_season.ipynb (for next_season.ipynb)
- next_season.ipynb (~7 mins, generates DF for all logs in current/upcoming season)
- pred_next_season.ipynb (generates DF with predictions with 0 predicted for every injured player)
- plottable_next_season.ipynb (pngs in plottable folder)


To do:
- extending data to previous seasons
- adjust xP for bonus
- force model to learn xP - avg Points
- try linear model
- price, transfers out/in as predictors
- compare old and new dataset and model
- streamlit - stats tab
- fill dataset with 0 min matches
- how many days from last match
- plottable folders
- EDA
- plottable color bug
- add description on page
- plottable add price
- form component (weighted by days that past)
- add bench to best eleven
- divider line above Summary
- store functions outside of notebooks
- MAE@N
- xP underestimated
- evaluation as DataFrame
- preds for more than 1 gameweek
- goalkeeper model
- plottable add captain icon
- is_penalty_taker features
- remove rows with 0 minutes played
- separate model for players with less than 10 caps registered
- investigate missing rows
- pairwise called in a wrong order
- optimize predict for positional model 
- solve performance issues - iterrows, apply 
- plots frontend
- 45 missing rows in nextseason
- estimate expected minutes
- refactor to stop using vaastav



- run global_scraper.py (~6 mins)
- run global_merger.py