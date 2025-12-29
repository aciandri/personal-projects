import streamlit as st
from core import DataLoader
from config.config import KAGGLE_DATASET, KAGGLE_FILE

dict_uploader_texts = st.session_state.translations["uploader_texts"]

def show_data_upload_page():
    """Pagina UI per upload dati"""
    
    flag_ita = st.session_state.language == 'it'
    # Inizializza loader
    if 'data_loader' not in st.session_state:
        st.session_state.data_loader = DataLoader()
    
    loader = st.session_state.data_loader
    
    # Scelta modalità caricamento
    use_default = st.checkbox(dict_uploader_texts["kaggle_checkbox"])
    
    uploaded_file = None
    if not use_default:
        uploaded_file = st.file_uploader(
            dict_uploader_texts["upload_file"],
            type=['csv', 'xlsx']
        )
    else:
        st.info(f"📁 Dataset: {KAGGLE_DATASET}/{KAGGLE_FILE}")
    
    # Bottone caricamento
    if st.button(dict_uploader_texts["load_data"]["initial"]):
        with st.spinner(dict_uploader_texts["load_data"]["loading"]):
            
            # Carica in base alla scelta
            if use_default:
                success = loader.load_kaggle_dataset(KAGGLE_DATASET, KAGGLE_FILE)
            elif uploaded_file:
                success = loader.load_from_fileobj(uploaded_file, uploaded_file.name)
            else:
                st.warning("Seleziona un file" if flag_ita else "Select a file")
                return
            
            # Feedback UI
            if success:
                st.success(
                    dict_uploader_texts["load_data"]["loaded"].replace("/nr_rows", str(loader.file_info['rows']))
                )   
                st.dataframe(loader.df.head())
                
                # Salva in session state per altre pagine
                st.session_state.df = loader.df
                st.session_state.data_loaded = True
            else:
                st.error(dict_uploader_texts["load_data"]["error"])

show_data_upload_page()