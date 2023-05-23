import os, sys
from src.logger import logging
from src.exception import CustmeException
from src.component.data_ingestion import DataIngestion
from src.component.data_transfromation import DataTransformation
from src.component.modrl_trainer import ModelTrainer
from dataclasses import dataclass

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.inititate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.inititate_data_transformation(train_data_path, test_data_path)
    model_training = ModelTrainer()
    model_training.inititate_model_trainer(train_arr, test_arr)

    # src\pipeline\training_pipeline.py