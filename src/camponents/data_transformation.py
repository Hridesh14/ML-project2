import sys
import os
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from src.exception import CustomException
from sklearn.pipeline import Pipeline
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfic:
    preprocessing_obj_path : str= os.path.join('artifects','preprocessing.pkl')

class DataTransformation():
    def __init__(self):
        self.Datatransformaitonconfig= DataTransformationConfic()
    
    def get_Data_Transformation(self):
        ''' 
        this function wil initate data trasformation
        '''

        try:
            cat_feature =['gender',
                         'race_ethnicity',
                         'parental_level_of_education',
                         'lunch',
                         'test_preparation_course'
                         ]
            num_feature =['math_score','reading_score','writing_score',]
            categorical_pipeline = Pipeline(
                steps=[
                    ('Imputer',SimpleImputer(strategy='most_frequent')),
                    ('OneHotencoder',OneHotEncoder())
                ]
            )
            numeric_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('Standerd_scaler',StandardScaler())
                ]

            )
            logging.info(f'categorical Feature:{cat_feature}')
            logging.info(f'Numerical Features:{num_feature}')

            preprocessor = ColumnTransformer(
                [
                    ('numerical_transformer',numeric_pipeline,num_feature),
                    ('categorical_transformer',categorical_pipeline,cat_feature)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('read train and test data')
            logging.info('initate preprocessor objective')
            Preprocessor_obj = self.get_Data_Transformation()

            target_feature_column = 'Average_score'

            input_feature_train_df = train_df.drop(columns=[target_feature_column],axis=1)
            traget_feature_train_df = train_df[target_feature_column]

            input_feature_test_df = test_df.drop(columns=[target_feature_column],axis=1)
            traget_feature_test_df= test_df[target_feature_column]

            logging.info('Apply Preprocessor obj to transformation train_data and test_data')
            
            input_feature_train_arr = Preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = Preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr ,np.array(traget_feature_train_df)
            ]
            test_arr =np.c_[
                input_feature_test_arr,np.array(traget_feature_test_df)
            ]

            save_object(file_path=DataTransformationConfic.preprocessing_obj_path,
                        obj = Preprocessor_obj)
            
            return (
                train_arr,
                test_arr,
                self.Datatransformaitonconfig.preprocessing_obj_path,
            )

        except Exception as e:
            raise CustomException(e,sys)
        

        