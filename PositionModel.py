from sklearn.ensemble import RandomForestRegressor

class PositionModel:
    def __init__(self):
        self.model = RandomForestRegressor(random_state=42)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
