import pandas as pd
import os 
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from src.camponents.data_transformation import DataTransformation
@dataclass
class DataIngestionconfig:
    train_data_path = os.path.join('artifects','train.csv')
    test_data_path = os.path.join('artifects','test.csv')
    row_data_path = os.path.join('artifects','data.csv')

class DataIngestion:
    def __init__(self):             
        self.dataingestionconfig=DataIngestionconfig()
    def initate_data_ingustion(self):
        logging.info('Entered the data ingustion methord')
        try:
         df =pd.read_csv('notebook\data\ new_stud.csv')
         os.makedirs(os.path.dirname(self.dataingestionconfig.test_data_path),exist_ok=True)
         df.to_csv(self.dataingestionconfig.row_data_path,index=False,header=True)
         logging.info('Train Test Split')
         train_set,test_set= train_test_split(df,test_size=0.25,random_state=42)
         train_set.to_csv(self.dataingestionconfig.train_data_path,index=False,header=True)
         test_set.to_csv(self.dataingestionconfig.test_data_path,index=False,header=True)
         logging.info('data_ingestion completed')
         return(
             self.dataingestionconfig.train_data_path,
             self.dataingestionconfig.test_data_path
         )
        except Exception as e:
           raise CustomException(e,sys)
if __name__=='__main__':
   obj = DataIngestion()
   train_data,test_data=obj.initate_data_ingustion()

   dtobj=DataTransformation()
   dtobj.initiate_data_transformation(train_data,test_data)

