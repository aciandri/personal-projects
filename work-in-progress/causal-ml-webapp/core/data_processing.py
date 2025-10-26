import pandas as pd
import kagglehub
import os
from utils.log_config import get_logger

logger = get_logger(__name__)

class DataLoader:
    """Carica e valida dati - SOLO logica, nessuna UI"""
    
    def __init__(self):
        self.df = None
        self.file_info = {}
    
    def load_from_path(self, file_path: str) -> bool:
        """Carica da percorso file"""
        try:
            if file_path.endswith('.csv'):
                self.df = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                self.df = pd.read_excel(file_path, sheet_name=0)
            else:
                raise ValueError(f"Formato non supportato: {file_path}")
            
            self._preprocess()
            logger.info(f"Caricati {len(self.df)} record da {file_path}")
            return True
            
        except Exception as e:
            logger.error(f"Errore caricamento {file_path}: {e}")
            return False
    
    def load_from_fileobj(self, file_obj, filename: str) -> bool:
        """Carica da oggetto file (es. Streamlit uploader)"""
        try:
            if filename.endswith('.csv'):
                self.df = pd.read_csv(file_obj)
            elif filename.endswith('.xlsx'):
                self.df = pd.read_excel(file_obj, sheet_name=0)
            else:
                raise ValueError(f"Formato non supportato: {filename}")
            
            self._preprocess()
            logger.info(f"Caricati {len(self.df)} record da upload")
            return True
            
        except Exception as e:
            logger.error(f"Errore caricamento upload: {e}")
            return False
    
    def load_kaggle_dataset(self, dataset_name: str, filename: str) -> bool:
        """Scarica e carica dataset Kaggle"""
        try:
            cache_path = self._get_kaggle_cache_path(dataset_name, filename)
            
            if os.path.exists(cache_path):
                logger.info("Dataset Kaggle trovato in cache")
                return self.load_from_path(cache_path)
            
            logger.info("Download dataset Kaggle...")
            downloaded_path = kagglehub.dataset_download(dataset_name)
            full_path = os.path.join(downloaded_path, filename)
            
            return self.load_from_path(full_path)
            
        except Exception as e:
            logger.error(f"Errore download Kaggle: {e}")
            return False
    
    def _preprocess(self):
        """Preprocessing standard"""
        if self.df is not None:
            self.df.columns = self.df.columns.str.upper()
            self.file_info = {
                'rows': len(self.df),
                'cols': len(self.df.columns),
                'columns': list(self.df.columns)
            }
    
    def _get_kaggle_cache_path(self, dataset_name: str, filename: str) -> str:
        base_cache = os.path.expanduser("~/.cache/kagglehub/datasets")
        return os.path.join(
            base_cache, 
            dataset_name.replace("/", os.sep), 
            "versions", "1", 
            filename
        )
    
    def validate(self, required_columns: list) -> bool:
        """Valida presenza colonne richieste"""
        if self.df is None:
            return False
        return all(col in self.df.columns for col in required_columns)