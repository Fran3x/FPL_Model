import sys
import pprint
import pandas as pd
 
sys.path.insert(0, 'C:/Users/user/Desktop/FPL_ML/vaastav')

from getters import *
from understat import *
from mergers import *
from cleaners import *

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt

#data = import_merged_gw('2021-22')
# print(data)
pp = pprint.PrettyPrinter()
#id_players('vaastav\data\cleaned_merged_seasons.csv', 'ids')

data = pd.read_csv('vaastav\data\cleaned_merged_seasons.csv')
salah = data[data['name'] == "Mohamed Salah"]
print('LENGTH:', len(salah))
#salah = salah.dropna(subset=['goals_scored', 'total_points'])
#print(len(salah))

rand_for = RandomForestRegressor(max_depth=8, random_state=0)

print(salah.columns)

X_train, X_test, y_train, y_test = train_test_split(salah[['goals_scored', 'assists', 'bps', 'was_home', 'creativity']], 
salah['total_points'], test_size=0.25, random_state=42, shuffle=False)

rand_for.fit(X_train, y_train)
y_pred = rand_for.predict(X_test)

print('MSE:', mean_squared_error(y_pred, y_test))

#pp.pprint(salah)
pd.DataFrame(salah).to_csv('example.csv')

# plt.scatter(X_test.index, y_test)
# plt.scatter(X_test.index, y_pred)
# plt.show()


from PointsPredictorModel import *

X_train, X_test, y_train, y_test = train_test_split(data[['goals_scored', 'assists', 'bps', 'was_home', 'creativity']], 
data['total_points'], test_size=0.25, random_state=42, shuffle=False)

points_model = PointsPredictorModel()
#points_model.fit(X_train, y_train)
#points_model.predict()

# kevin = get_player_data(447)
# # [0] - appearances
# # [1] - shots
# kevin = pd.DataFrame(kevin[0])
# pp.pprint(kevin)
# kevin.to_csv('example.csv')

epl = get_epl_data()[1]
epl = pd.DataFrame(epl)
epl.to_csv('example.csv')
pp.pprint(epl)


from data_prep import *
# d = get_dataset()

# pp.pprint(d)
# d.to_csv('example.csv')

# X_train, X_test, y_train, y_test = train_test_split(d[['shots', 'goals']], d['xG'], test_size=0.25, random_state=42, shuffle=False)

points_model = PointsPredictorModel()
points_model.fit(X_train.values, y_train.values)

print(points_model.predict([[3, 1]]))