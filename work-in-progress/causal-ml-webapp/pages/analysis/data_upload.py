import streamlit as st
from core import DataLoader
from config.config import KAGGLE_DATASET, KAGGLE_FILE

def show_data_upload_page():
    """Pagina UI per upload dati"""
    
    flag_ita = st.session_state.language == 'it'
    # Inizializza loader
    if 'data_loader' not in st.session_state:
        st.session_state.data_loader = DataLoader()
    
    loader = st.session_state.data_loader
    
    # Scelta modalità caricamento
    use_default = st.checkbox(
        "Usa dataset Kaggle di default" if flag_ita else "Use default Kaggle dataset"
    )
    
    uploaded_file = None
    if not use_default:
        uploaded_file = st.file_uploader(
            "Carica file" if flag_ita else "Upload file",
            type=['csv', 'xlsx']
        )
    else:
        st.info(f"📁 Dataset: {KAGGLE_DATASET}/{KAGGLE_FILE}")
    
    # Bottone caricamento
    if st.button("Carica dati" if flag_ita else "Load data"):
        with st.spinner("Caricamento in corso..." if flag_ita else "Loading..."):
            
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
                    f"✅ Caricati {loader.file_info['rows']} record" 
                    if flag_ita else 
                    f"✅ Loaded {loader.file_info['rows']} records"
                )
                st.dataframe(loader.df.head())
                
                # Salva in session state per altre pagine
                st.session_state.df = loader.df
                st.session_state.data_loaded = True
            else:
                st.error(
                    "❌ Errore durante il caricamento" 
                    if flag_ita else 
                    "❌ Error loading data"
                )

show_data_upload_page()