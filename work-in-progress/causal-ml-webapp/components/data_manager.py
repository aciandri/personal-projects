import streamlit as st
import pandas as pd
import kagglehub
from log_config import get_logger

logger = get_logger(__name__)

# Download latest version
path_to_kaggle_df = kagglehub.dataset_download("arashnic/uplift-modeling")
kaggle_file = f"{path_to_kaggle_df}/uplift_modeling.csv"

class DataManager():
    def __init__(self, dict_texts: dict):
        self.df = pd.DataFrame()
        self.dict_texts = dict_texts

        if "uploaded_file" not in st.session_state:
            st.session_state["uploaded_file"] = kaggle_file

    def file_upload(self) -> str:
        """ 
        Caricamento del file.

        Returns:
            self.uploaded_file (str): Nome del file caricato dall'utente.
        """

        cols = st.columns([1,2,4,1])
        cols[1].write("")

        # Choose either to upload a file or to continue with the default file
        if st.button("Choose an excel file to upload"):
            uploaded_file = cols[2].file_uploader(
                    label="uploader", type=["xlsx"], label_visibility="collapsed"
                )
        else:
            uploaded_file = f"{path_to_kaggle_df}/uplift_modeling.csv"
        
        # If the user presses the button to continue with the analysis, then update the session state
        if st.button("Continua con l'analisi" if self.flag_ita else "Continue with the analysis"):
            if st.session_state["uploaded_file"] != uploaded_file:
                st.session_state["uploaded_file"] = uploaded_file
        else:
            if st.session_state["uploaded_file"] != uploaded_file:
                uploaded_file = st.session_state["uploaded_file"]

        self._read_data(uploaded_file=uploaded_file)
        return False # TODO: levarlo e mettere questo return nelle fasi successive, magari un bottone di run finale
    
    def _read_data(self, uploaded_file):
        """ 
        Carica i dati dal file Excel e salva i nomi dei fogli. 
        Converte i nomi delle colonne in maiuscolo.
        Il primo foglio deve contenere i dati.
        """
        
        try:
            self.sheet_names = pd.ExcelFile(uploaded_file).sheet_names
            self.df = pd.read_excel(uploaded_file, sheet_name = self.sheet_names[0]) 
            self.df.columns =  self.df.columns.str.upper()
        except:
            logger.error(f"{'Il file non è congruente con il formato atteso' if self.flag_ita else 'The file doesn t match the expected format'}")




