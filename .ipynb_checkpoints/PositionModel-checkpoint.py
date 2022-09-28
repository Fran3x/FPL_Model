from sklearn.ensemble import RandomForestRegressor

class PositionModel:
    def __init__(self):
        self.gk_model = RandomForestRegressor(random_state=42)
        self.def_model = RandomForestRegressor(random_state=42)
        self.mid_model = RandomForestRegressor(random_state=42)
        self.fwd_model = RandomForestRegressor(random_state=42)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

