import dill
import os
import sys
from src.exceptions import custom_exception
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
def save_bin(file_path,obj):

        try:
            dir_path=os.path.dirname(file_path)
            os.makedirs(dir_path,exist_ok=True)
            with open(file_path,"wb") as file_obj:
                 dill.dump(obj,file_obj)
        
        except Exception as e:
            raise custom_exception(e,sys)
def evaluate_models(X_train,y_train,X_test,y_test,models,param):
     try:
          score={}
          for index in range(len(list(models))):
               para=param[list(models.keys())[index]]
               model=list(models.values())[index]
               gs=GridSearchCV(model,para,cv=3)
               gs.fit(X_train,y_train)
               model.set_params(**gs.best_params_)
               model.fit(X_train,y_train)
               test_predict=model.predict(X_test)
               test_data_score=r2_score(y_test,test_predict)
               score[list(models.keys())[index]]=test_data_score
          return score


     except Exception as e:
          raise custom_exception(e,sys)