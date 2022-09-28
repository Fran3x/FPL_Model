from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import datetime

def split_data(df, predictors, to_predict, train_size=0.85):
    X_train, X_test, y_train, y_test = train_test_split(df[predictors], df[to_predict], train_size=train_size, random_state=42)
    return X_train, X_test, y_train, y_test


def get_metrics(y_true, y_pred):
    mse = mean_squared_error(y_pred, y_true)
    mae = mean_absolute_error(y_pred, y_true)
    r2 = r2_score(y_pred, y_true)
    return {
        'mse': mse,
        'mae': mae,
        'r2': r2
    }


CURRENT_SEASON_FPL = '2022-23'
CURRENT_SEASON_UNDERSTAT = '2022'
NEXT_GAMEWEEK = 9
NEXT_GAMEWEEK_DATE = datetime.datetime(2022, 9, 30)