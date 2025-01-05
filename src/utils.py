import os 
import sys
import dill
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
        
        for i in range(len(models)):
            model = list(models.values())[i]
            model_name = list(models.keys())[i]
            
            para = param.get(model_name, {})

            grid = GridSearchCV(model, para, cv=3)
            grid.fit(X_train, y_train)
            
            model.set_params(**grid.best_params_)
            model.fit(X_train, y_train)
            
            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)
            
            train_model_score = r2_score(y_train, y_pred_train)
            test_model_score = r2_score(y_test, y_pred_test)

            report[model_name] = test_model_score
        
        return report   
        
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)