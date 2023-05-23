from src.logger import logging
from src.exception import CustmeException
import os, sys
import pickle
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_curve, f1_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok= True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustmeException(e, sys)
    

def evaluate_model(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = params[list(models.keys())[i]]

            GS = GridSearchCV(model, para, cv = 5)
            GS.fit(X_train, y_train)

            model.set_params(**GS.best_params_)
            model.fit(X_train, y_train)

            # make prediction
            y_pred = model.predict(X_test)
            test_model_acuracy = accuracy_score(y_test, y_pred)

            report[list(models.values())[i]] = test_model_acuracy

            return report

    except Exception as e:
        raise CustmeException(e, sys)
