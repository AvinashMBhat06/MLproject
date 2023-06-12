import os
from dataclasses import dataclass
from src.logger import logging
from src.exceptions import custom_exception
from sklearn.tree import DecisionTreeRegressor
from src.utils import evaluate_models
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.utils import save_bin
from catboost import CatBoostRegressor
import sys
@dataclass
class Model_trainerconfig:
    file_path=os.path.join("Datasets","Modelconfig.pkl")
class model_trainer:
    def __init__(self):
        self.model=Model_trainerconfig()
    def iniate_model_trainer(self,train_data,test_data):
        try:
            logging.info("Spliting test input and output")
            X_train,y_train,X_test,y_test=(
                train_data[:,:-1],
                train_data[:,-1],
                test_data[:,:-1],
                test_data[:,-1]
            )
            models={
                "Random Forest":RandomForestRegressor(),
                "Decision Tree":DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Classifier": KNeighborsRegressor(),
                "XGBClassifier": XGBRegressor(),
                "CatBoosting Classifier": CatBoostRegressor(verbose=False),
                "AdaBoost Classifier": AdaBoostRegressor()
            }
            model_report=evaluate_models(X_train,y_train,X_test,y_test,models)
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_bin(
                file_path=self.model.file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            print(r2_square,' --- ',best_model_name)
            
        except Exception as e:
            raise custom_exception(e,sys)
    