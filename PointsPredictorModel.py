from sklearn.ensemble import RandomForestRegressor

class PointsPredictorModel:
    # predicts how many points will player score having some preestimated values
    # 1. predicted xG
    # 2. predicted xA
    # 3. predicted CS
    # 4. predicted bps
    def __init__(self):
        # later dictionary of submodels
        # model for midfielders
        self.mid_model = RandomForestRegressor()

    def fit(self, X, y):
        # best to fit on whole dataset
        
        # takes only midfields
        self.mid_model.fit(X, y)

    def predict(self, X):
        return self.mid_model.predict(X)