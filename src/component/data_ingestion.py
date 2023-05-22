import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustmeException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.component.data_transfromation import DataTransformation

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts/data_ingestion", "train.csv")
    test_data_path = os.path.join("artifacts/data_ingestion", "test.csv")
    raw_data_path = os.path.join("artifacts/data_ingestion", "raw.csv")

# notbook\data\income_cleandata.csv

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def inititate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            logging.info("Data Reading using Pandas library from local system")
            data = pd.read_csv(os.path.join("notbook/data", "income_cleandata.csv"))
            logging.info("Data Reading completed")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Dat spliteted into train and test")

            train_set, test_set = train_test_split(data, test_size = .30, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info("Data Ingestion completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            logging.info("Erro occured in data ingestion stage")
            raise CustmeException(e, sys)

if __name__ =="__main__":
    obj = DataIngestion()
    treain_data_path , test_data_path = obj.inititate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.inititate_data_transformation(treain_data_path , test_data_path)





# src\component\data_ingestion.py