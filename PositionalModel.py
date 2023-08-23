from xgboost import XGBRegressor
import numpy as np

class PositionalModel:
    def __init__(self, features, to_predict, model_GK=None, model_DEF=None, model_MID=None, model_FWD=None):
        self.features = features
        self.to_predict = to_predict
        
        if model_GK:
            self.model_GK = model_GK
        else:
            self.model_GK = XGBRegressor(
                random_state=42, verbosity = 0,
                # n_estimators=500,
                # early_stopping_rounds=5,
                # learning_rate=0.2
            )
        
        if model_DEF:
            self.model_DEF = model_DEF
        else:
            self.model_DEF = XGBRegressor(
                random_state=42, verbosity = 0,
                n_estimators=500,
                early_stopping_rounds=5,
                learning_rate=0.2
            )
        
        if model_MID:
            self.model_MID = model_MID
        else:
            self.model_MID = XGBRegressor(
                random_state=42, verbosity = 0,
                n_estimators=500,
                early_stopping_rounds=5,
                learning_rate=0.2
            )
        
        if model_FWD:
            self.model_FWD = model_FWD
        else:
            self.model_FWD = XGBRegressor(
                random_state=42, verbosity = 0,
                n_estimators=500,
                early_stopping_rounds=5,
                learning_rate=0.2
            )
            
        # self.assign_custom_predicts()
        
        
    def fit(self, X, y, X_valid, y_valid):
        # print(y[y["FPL_pos"] == "GK"].shape)
        self.model_GK.fit(X[X["FPL_pos"] == "GK"][self.features], y[y["FPL_pos"] == "GK"][self.to_predict],
        # eval_set=[(X_valid[X_valid["FPL_pos"] == "GK"][self.features], y_valid[y_valid["FPL_pos"] == "GK"][self.to_predict])],
        verbose=False)
        self.model_DEF.fit(X[X["FPL_pos"] == "DEF"][self.features], y[y["FPL_pos"] == "DEF"][self.to_predict],
        eval_set=[(X_valid[X_valid["FPL_pos"] == "DEF"][self.features], y_valid[y_valid["FPL_pos"] == "DEF"][self.to_predict])],
        verbose=False)
        self.model_MID.fit(X[X["FPL_pos"] == "MID"][self.features], y[y["FPL_pos"] == "MID"][self.to_predict],
        eval_set=[(X_valid[X_valid["FPL_pos"] == "MID"][self.features], y_valid[y_valid["FPL_pos"] == "MID"][self.to_predict])],
        verbose=False)
        self.model_FWD.fit(X[X["FPL_pos"] == "FWD"][self.features], y[y["FPL_pos"] == "FWD"][self.to_predict],
        eval_set=[(X_valid[X_valid["FPL_pos"] == "FWD"][self.features], y_valid[y_valid["FPL_pos"] == "FWD"][self.to_predict])],
        verbose=False)
        
    def predict(self, X):
        output = []
        i = 0
        for ind, row in X.iterrows():
            # print(i)
            if row["FPL_pos"] == "GK":
                output.append( self.model_GK.predict( X.head(i+1).tail(1)[self.features] ) )
            if row["FPL_pos"] == "DEF":
                # print(row[features])
                output.append( self.model_DEF.predict( X.head(i+1).tail(1)[self.features] ) )
            if row["FPL_pos"] == "MID":
                output.append( self.model_MID.predict( X.head(i+1).tail(1)[self.features] ) )
            if row["FPL_pos"] == "FWD":
                output.append( self.model_FWD.predict( X.head(i+1).tail(1)[self.features] ) )
            i += 1
        return np.array(output).flatten()
    
    def custom_predict_fwd(self, X):
            XGB_COMPONENT = 0.45
            OVERALL_COMPONENT = 0.5
            FORM_COMPONENT = 0.25

            model_pred = np.array(self.model_FWD.predict_old(X))
            overall_pred = np.array([row["Avg_FPL_points"] for i, row in X.iterrows()])
            form_pred = np.array([row["FPL_points_4"] for i, row in X.iterrows()])

            return np.add( model_pred * XGB_COMPONENT, overall_pred * OVERALL_COMPONENT, form_pred * FORM_COMPONENT )
    
    def assign_custom_predicts(self):
        # self.custom_predict_fwd = custom_predict_fwd

        self.model_FWD.predict_old = self.model_FWD.predict
        self.model_FWD.predict = self.custom_predict_fwd