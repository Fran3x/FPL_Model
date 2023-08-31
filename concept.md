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
- get_players.ipynb (to scrape current players for every team from fbref)
- run global_scraper.py (~6 mins)
- run global_merger.py
- move master_team_list.csv from /vaastav to /data (only at the start of new season)
- FPL_players.ipynb
- fbref_scrape.ipynb to get all fbref data (~30 mins per season)
- merge_FPL_fbref.ipynb
- team_elo_rating.ipynb (to get newest elo ratings)
- assign_team_to_previous.ipynb (~9 mins)
- dataset_cleaning.csv (renaming columns etc.)


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
- gk_last_season.ipynb (to adjusting GKs with low number of games played)
- df_features_for_next_season.ipynb (for next_season.ipynb)
- next_season.ipynb (~7 mins, generates DF for all logs in current/upcoming season)
- pred_next_season.ipynb (generates DF with predictions with 0 predicted for every injured player)
- plottable_next_season.ipynb (pngs in plottable folder)


To do:
- extending data to previous seasons
- force model to learn xP - avg Points
- try linear model
- compare old and new dataset and model
- streamlit - stats tab
- fill dataset with 0 min matches
- how many days from last match
- plottable folders
- plottable color bug
- add descriptions on page
- form component (weighted by days that past)
- add bench to best eleven
- divider line above Summary
- store functions outside of notebooks
- MAE@N
- xP underestimated
- evaluation as DataFrame
- preds for more than 1 gameweek
- plottable add captain icon
- is_penalty_taker features
- remove rows with 0 minutes played
- separate model for players with less than 10 caps registered
- investigate missing rows
- pairwise called in a wrong order
- solve performance issues - iterrows, apply 
- plots frontend
- 45 missing rows in nextseason
- estimate expected minutes
- use footballers photos to visualize first 11
- information about when was data updated for the last time
- form xP and xP_avg_points
- dynamically save features to file
- use web name
- average value of prediction in evaluation
- xgb custom loss function - weighted MSE?
- save features to file
- model more things directly
- target encoding for position
- next_season.ipynb output is actually lagged by 1 gameweek
- metric only for selected by more than p%
- linear for every position