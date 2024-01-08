import os
import urllib.request as request 
import zipfile
from pathlib import Path
from src.wineProject import logger
from src.wineProject.utils.common import get_size
from src.wineProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info \n{headers}")
        else:
            logger.info(f"File already exists of size {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extract the zip file into the dta direcory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            