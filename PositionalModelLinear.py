from xgboost import XGBRegressor
from sklearn.ensemble import GradientBoostingRegressor
from catboost import CatBoostRegressor
import numpy as np
from sklearn.linear_model import LinearRegression

class PositionalModelLinear:
    def __init__(self, features_GK, features_outfield, cat_features, to_predict, model_GK=None, model_outfield=None,):
        self.features_GK = features_GK
        self.features_outfield = features_outfield
        self.cat_features = cat_features
        self.to_predict = to_predict
        
        if model_GK:
            self.model_GK = model_GK
        else:
            # self.model_GK = CatBoostRegressor(
            #     random_state=42, 
            #     verbose = False
            #     # verbosity = 0,
            #     # n_estimators=500,
            #     # early_stopping_rounds=5,
            #     # learning_rate=0.2
            # )
            self.model_GK = LinearRegression()
            
        if model_outfield:
            self.model_outfield = model_outfield
        else:
            self.model_outfield = LinearRegression()
        
        
    def fit(self, X, y):
        if X[X["FPL_pos"] == "GK"].size > 0:
            self.model_GK.fit(X[X["FPL_pos"] == "GK"][self.features_GK], y[y["FPL_pos"] == "GK"][self.to_predict])
        if X[X["FPL_pos"] != "GK"].size > 0:
            self.model_outfield.fit(X[X["FPL_pos"] != "GK"][self.features_outfield + self.cat_features], y[y["FPL_pos"] != "GK"][self.to_predict])
        
    def predict(self, X):
        X_preds = X.copy()
        if X_preds[X_preds["FPL_pos"] == "GK"].size > 0:
            X_preds.loc[X_preds["FPL_pos"] == "GK", "Pred"] =  self.model_GK.predict( X_preds[X_preds["FPL_pos"] == "GK"][self.features_GK] )
        if X_preds[X_preds["FPL_pos"] != "GK"].size > 0:
            X_preds.loc[X_preds["FPL_pos"] != "GK", "Pred"] =  self.model_outfield.predict( X_preds[X_preds["FPL_pos"] != "GK"][self.features_outfield + self.cat_features] )
        return X_preds["Pred"].to_list()