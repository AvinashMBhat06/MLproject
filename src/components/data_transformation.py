import sys
from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.exceptions import custom_exception
from src.logger import logging
import pandas as pd
from dataclasses import dataclass
import os
import numpy as np
from src.utils import save_bin

@dataclass
class data_transformationConfig:
    preprocessor_obj_file_path=os.path.join('Datasets',"preprocessor.pkl")
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=data_transformationConfig()

    def data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )
            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )


            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ])
            return preprocessor
        except Exception as e:
            raise custom_exception(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
            try:
                train_pd=pd.read_csv(train_path)
                test_pd=pd.read_csv(test_path)

                logging.info("Obtaining preprocessing object")
                preprocessing_obj=self.data_transformer_object()
                target_column_name="math_score"
                target_feature_train_df=train_pd[target_column_name]
                target_feature_test_df=test_pd[target_column_name]
                input_feature_train_df=train_pd.drop(columns=[target_column_name],axis=1)
                input_feature_test_df=test_pd.drop(columns=[target_column_name],axis=1)

                logging.info(
                    f"Applying preprocessing object on training dataframe and testing dataframe."
                )

                input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
                input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
                
                train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
                test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]


                
                logging.info(f"Saved preprocessing object.")

                save_bin(file_path=self.data_transformation_config.preprocessor_obj_file_path,obj=preprocessing_obj)

                return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            except Exception as e:
                raise custom_exception(e,sys)