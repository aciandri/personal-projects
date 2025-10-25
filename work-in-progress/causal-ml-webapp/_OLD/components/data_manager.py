# ----- Libraries -----
import streamlit as st
import pandas as pd
import kagglehub
import os
from .log_config import get_logger

logger = get_logger(__name__)

# ----- Kaggle Variables -----
# Download latest version
KAGGLE_DATASET = "arashnic/uplift-modeling"

# Percorso previsto del dataset nella cache di KaggleHub
BASE_CACHE_PATH = os.path.expanduser("~/.cache/kagglehub/datasets")
LOCAL_PATH = os.path.join(BASE_CACHE_PATH, KAGGLE_DATASET.replace("/", os.sep), "versions", "1")
KAGGLE_FILE = "criteo-uplift-v2.1.csv"
PATH_TO_KAGGLE_DF = os.path.join(LOCAL_PATH, KAGGLE_FILE)

# ----- Data Manager -----
class DataManager():
    def __init__(self, dict_texts: dict, flag_ita: bool):
        self.df = pd.DataFrame()
        self.dict_texts = dict_texts
        self.flag_ita = flag_ita

        if "uploaded_file" not in st.session_state:
            st.session_state["uploaded_file"] = KAGGLE_FILE

    def file_upload(self) -> str:
        """ 
        Caricamento del file.

        Returns:
            self.uploaded_file (str): Nome del file caricato dall'utente.
        """

        cols = st.columns([1,2,4,1])
        cols[1].write("")

        # Choose either to upload a file or to continue with the default file
        if st.checkbox("Scegli un file da caricare" if self.flag_ita else "Choose a file to upload"):
            uploaded_file = st.file_uploader(
                    label="uploader", type=["xlsx"], label_visibility="collapsed"
                )
        else:
            uploaded_file = KAGGLE_FILE
            st.button(label=f"Default file to load: {DEFAULT_FILE} ", icon=":material/database_upload:", disabled=True)

        
        # If the user presses the button to continue with the analysis, then update the session state
        if st.button("Continua con l'analisi" if self.flag_ita else "Continue with the analysis"):
            if st.session_state["uploaded_file"] != uploaded_file:
                st.session_state["uploaded_file"] = uploaded_file
        else:
            if st.session_state["uploaded_file"] != uploaded_file:
                uploaded_file = st.session_state["uploaded_file"]

        self._load_file(uploaded_file=uploaded_file)
        return False # TODO: levarlo e mettere questo return nelle fasi successive, magari un bottone di run finale
    
    def _load_file(self, uploaded_file):
        # Se è un oggetto Streamlit (ha attributo .name)
        if hasattr(uploaded_file, "name"):
            filename = uploaded_file.name.lower()
        else:
            filename = str(uploaded_file).lower()

        try:
            if filename.endswith(".xlsx"):
                # Se è file-like (es. da Streamlit)
                if hasattr(uploaded_file, "read"):
                    xls = pd.ExcelFile(uploaded_file)
                else:
                    if uploaded_file == KAGGLE_FILE:
                        self._get_kaggle_file()
                    xls = pd.ExcelFile(os.path.abspath(uploaded_file))
                sheet_names = xls.sheet_names
                df = pd.read_excel(xls, sheet_name=sheet_names[0])
            elif filename.endswith(".csv"):
                if hasattr(uploaded_file, "read"):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_csv(os.path.abspath(uploaded_file))
            else:
                raise ValueError("Formato non supportato: usa un file .csv o .xlsx")

            df.columns = df.columns.str.upper()
            return df

        except Exception as e:
            raise RuntimeError(f"❌ Caricamento non riuscito per il file {uploaded_file}: {e}")

    def _get_kaggle_file(self):
        # 🔸 Se il file non esiste, scaricalo
        if not os.path.exists(KAGGLE_FILE):
            print("📦 Download del dataset da Kaggle (prima volta)...")
            PATH_TO_KAGGLE_DF = kagglehub.dataset_download(KAGGLE_DATASET)
            KAGGLE_FILE = os.path.join(PATH_TO_KAGGLE_DF, KAGGLE_FILE)
        else:
            print("✅ Dataset già disponibile in cache, riuso del file locale.")

        print("📁 File pronto:", KAGGLE_FILE)



