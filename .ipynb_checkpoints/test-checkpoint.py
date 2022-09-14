from data_prep import *
from PositionModel import *
from PlayerModel import *
from commons import *


# predictors = ['goals_scored', 'assists_fpl', 'bps', 'penalties_missed', 
# 'clean_sheets', 'yellow_cards', 'red_cards', 'minutes', 'own_goals']
predictors = ['goals_avg5', 'xG_avg5', 'assists_fpl_avg5',
       'bonus_avg5', 'bps_avg5', 'clean_sheets_avg5', 'goals_conceded_avg5',
       'shots_avg5', 'xGBuildup_avg5', 'xGChain_avg5', 'yellow_cards_avg5',
       'red_cards_avg5', 'was_home']
rolling_columns = ['goals', 'xG', 'assists_fpl', 'bonus', 'bps', 'clean_sheets', 'goals_conceded', 'shots', 'xGBuildup', 'xGChain', 'yellow_cards', 'red_cards']
to_predict = 'total_points'

# loading dataset
# df = merged_understat_and_fpl(rolling_columns, True)
df = load_dataset()
print(df.columns)

# general model
print('GENERAL MODEL:')
X_train, X_test, y_train, y_test = split_data(df, predictors, to_predict)
general_model = PositionModel()
general_model.fit(X_train, y_train)
y_pred = general_model.predict(X_test)
metrics = get_metrics(y_test, y_pred)
print(metrics)


# position model (MID)
print('POSITION MODEL:')
df_mid = df[df['position_fpl'] == 'MID']
X_train, X_test, y_train, y_test = split_data(df_mid, predictors, to_predict)
position_model = PositionModel()
position_model.fit(X_train, y_train)
y_pred = position_model.predict(X_test)
metrics = get_metrics(y_test, y_pred)
print(metrics)


# salah only
print('PLAYER MODEL:')
salah = df[df['name'] == 'Mohamed Salah']
X_train, X_test, y_train, y_test = split_data(salah, predictors, to_predict, 0.8)
position_model = PlayerModel()
position_model.fit(X_train, y_train)
y_pred = position_model.predict(X_test)
metrics = get_metrics(y_test, y_pred)
print(metrics)