from xgboost import XGBRegressor
import numpy as np

class PositionalModel:
    def __init__(self, features_GK, features_outfield, to_predict, model_GK=None, model_outfield=None):
        self.features_GK = features_GK
        self.features_outfield = features_outfield
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
            
        if model_outfield:
            self.model_outfield = model_outfield
        else:
            self.model_outfield = XGBRegressor(
                random_state=42, verbosity = 0,
                # n_estimators=500,
                # early_stopping_rounds=5,
                # learning_rate=0.2
            )
            
        self.assign_custom_predicts()
        
        
    def fit(self, X, y, X_valid, y_valid):
        # print(y[y["FPL_pos"] == "GK"].shape)
        self.model_GK.fit(X[X["FPL_pos"] == "GK"][self.features_GK], y[y["FPL_pos"] == "GK"][self.to_predict],
        # eval_set=[(X_valid[X_valid["FPL_pos"] == "GK"][self.features_GK], y_valid[y_valid["FPL_pos"] == "GK"][self.to_predict])],
        verbose=False)
        self.model_outfield.fit(X[X["FPL_pos"] != "GK"][self.features_outfield], y[y["FPL_pos"] != "GK"][self.to_predict],
        # eval_set=[(X_valid[X_valid["FPL_pos"] != "GK"][self.features_outfield], y_valid[y_valid["FPL_pos"] != "GK"][self.to_predict])],
        verbose=False)
        
    def predict(self, X):
        X_preds = X.copy()
        # print(X_preds[X_preds["FPL_pos"] == "GK"].shape, X_preds[X_preds["FPL_pos"] == "GK"][self.features_GK].shape, self.model_GK.predict( X_preds[X_preds["FPL_pos"] == "GK"][self.features_GK] ).shape)
        if X_preds[X_preds["FPL_pos"] == "GK"].size > 0:
            X_preds.loc[X_preds["FPL_pos"] == "GK", "Pred"] =  self.model_GK.predict( X_preds[X_preds["FPL_pos"] == "GK"][self.features_GK] )
        if X_preds[X_preds["FPL_pos"] != "GK"].size > 0:
            X_preds.loc[X_preds["FPL_pos"] != "GK", "Pred"] =  self.model_outfield.predict( X_preds[X_preds["FPL_pos"] != "GK"][self.features_outfield] )
        return X_preds["Pred"].to_list()
        # output = []
        # i = 0
        # for ind, row in X.iterrows():
        #     # print(i)
        #     if row["FPL_pos"] == "GK":
        #         output.append( self.model_GK.predict( X.head(i+1).tail(1)[self.features_GK] ) )
        #     if row["FPL_pos"] != "GK":
        #         output.append( self.model_outfield.predict( X.head(i+1).tail(1)[self.features_outfield] ) )
        #     i += 1
        # return np.array(output).flatten()
    
    def custom_predict_GK(self, X):
            XGB_COMPONENT = 0.3
            OVERALL_COMPONENT = 0.67
            FORM_COMPONENT = 0.2

            model_pred = np.array(self.model_GK.predict_old(X))
            overall_pred = np.array([row["Avg_FPL_points"] for i, row in X.iterrows()])
            form_pred = np.array([row["FPL_points_4"] for i, row in X.iterrows()])

            return np.add( model_pred * XGB_COMPONENT, overall_pred * OVERALL_COMPONENT, form_pred * FORM_COMPONENT )
    
    def custom_predict_outfield(self, X):
            XGB_COMPONENT = 0.45
            OVERALL_COMPONENT = 0.5
            FORM_COMPONENT = 0.25

            model_pred = np.array(self.model_outfield.predict_old(X))
            overall_pred = np.array([row["Avg_FPL_points"] for i, row in X.iterrows()])
            form_pred = np.array([row["FPL_points_4"] for i, row in X.iterrows()])

            return np.add( model_pred * XGB_COMPONENT, overall_pred * OVERALL_COMPONENT, form_pred * FORM_COMPONENT )
    
    def assign_custom_predicts(self):
        self.model_outfield.predict_old = self.model_outfield.predict
        self.model_outfield.predict = self.custom_predict_outfield
        
        self.model_GK.predict_old = self.model_GK.predict
        self.model_GK.predict = self.custom_predict_GK