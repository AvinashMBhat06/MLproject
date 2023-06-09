import os
import sys
from src.exceptions import custom_exception
from src.logger import logging
from sklearn.model_selection import train_test_split
import pandas as pd
from dataclasses import dataclass
from src.components.data_transformation import data_transformationConfig
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import Model_trainerconfig
from src.components.model_trainer import model_trainer

@dataclass
class Data_ingesion_pathdata:
    train_dataset_path: str=os.path.join("Datasets","train.csv")
    test_dataset_path:  str=os.path.join("Datasets","test.csv")
    raw_dataset_path:   str=os.path.join("Datasets","rawD.csv")
class Data_ingestion:
    def __init__(self):
        self.ingestion=Data_ingesion_pathdata()
    def ingestion_intiation(self):
        logging.info("Data Ingestion Has Begun")
        try:
            os.makedirs(os.path.dirname(self.ingestion.train_dataset_path),exist_ok=True)
            df=pd.read_csv("data/stud.csv")
            df.to_csv(self.ingestion.raw_dataset_path,header=True,index=False)
            logging.info("Train-Test set split initiated")
            train_set,test_set=train_test_split(df,test_size=0.25,random_state=42)
            train_set.to_csv(self.ingestion.train_dataset_path,header=True,index=False)
            test_set.to_csv(self.ingestion.test_dataset_path,header=True,index=False)
            logging.info("Split completed")
            return (self.ingestion.test_dataset_path,
                self.ingestion.train_dataset_path)

        except Exception as e:
            raise custom_exception(e,sys)
        
if __name__=="__main__":
     data_ingestion_Obj=Data_ingestion()
     train_data_path,test_data_path=data_ingestion_Obj.ingestion_intiation()
     data_transformation_Obj=DataTransformation()
     train_data,test_data,_=data_transformation_Obj.initiate_data_transformation(train_data_path,test_data_path)
     model_trainer_obj=model_trainer()
     model_trainer_obj.iniate_model_trainer(train_data,test_data)

   
