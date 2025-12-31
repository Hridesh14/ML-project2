import pandas as pd
import os 
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
@dataclass
class Dataingustionconfig:
    Train_data_path: str =os.path.join('artifects','Train.csv')
    Test_data_path: str = os.path.join('artifects','Test.csv')
    raw_data_path: str = os.path.join('artifects','Raw.csv')


class Dataingestion:
    def __init__(self):
        self.ingestion_config = Dataingustionconfig()
    def initate_data_ingestion(self):
        logging.info('initate data ingestion methord')
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('read the data set from dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.Train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info('Train Test split')
            train_file,test_file = train_test_split(df,test_size=0.20,random_state=41)
            
            train_file.to_csv(self.ingestion_config.Train_data_path,index=False,header=True)
            test_file.to_csv(self.ingestion_config.Test_data_path,index=False,header=True)

            logging.info('ingestion is completed')
            return(
                self.ingestion_config.Train_data_path,
                self.ingestion_config.Test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
if __name__=='__main__':
    obj =Dataingestion()
    obj.initate_data_ingestion()


