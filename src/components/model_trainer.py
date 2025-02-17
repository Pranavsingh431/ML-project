import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("split train and test data")
            X_train, y_train, X_test, y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                'Random Forest':RandomForestRegressor(),
                'linear regression':LinearRegression(),
                'K nearest neighbors':KNeighborsRegressor(),
                'Decision tree':DecisionTreeRegressor(),
                'Adaboost':AdaBoostRegressor()
            }
            
            params = {
                'Decision tree': {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson']
                },
                
                'Random Forest':{
                    'n_estimators': [8,16,32,64,128,256]
                },
                
                'linear regression':{},
                
                'Adaboost':{
                    'learning_rate':[.1,.01,0.5,.001],
                    'n_estimators': [8,16,32,64,128,256]
                }
            }
            
            model_report:dict = evaluate_model(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models, param=params)
            
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]
            
            
            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info('best model found on training and testing data')
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            
            prediction = best_model.predict(X_test)
            
            r2 = r2_score(y_test, prediction)
            return r2
        
        except Exception as e:
            raise CustomException(e, sys)