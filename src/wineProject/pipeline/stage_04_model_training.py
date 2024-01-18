from src.wineProject import logger
from src.wineProject.config.configuration import ConfigurationManager
from src.wineProject.components.model_training import ModelTraining
from pathlib import Path



STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_training_config()
        model_training_config = ModelTraining(config=model_training_config)
        model_training_config.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e