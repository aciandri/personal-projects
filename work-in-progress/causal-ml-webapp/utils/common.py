# ----- Libraries -----
from pathlib import Path
import streamlit as st
import json
import os

from .log_config import get_logger

# ----- Logging -----
logger = get_logger(__name__)

# ----- Variables -----
TEXT_PATH = os.path.join(os.path.dirname(__file__), "texts")

# ----- Get JSON files -----
def load_json(flag_ita: bool, 
              file_json: str,
              directory: str = f"{TEXT_PATH}") -> dict:
    """
    Loads the JSON file and extracts a dictionary.

    Args:
        flag_ita (bool): True if the language is set to "Italian".
        file_json (str): Name of the JSON file without extension and directory.

    Returns:
        Dictionary with the checks to be performed or the readme.
    """

    try:
        with open(f"{directory}/{file_json}.json", "r", encoding="utf-8") as f:
            raw_controls = json.load(f)
        lang = "ita" if flag_ita else "eng"

        if file_json == 'texts':
            dictionary = {
                key: value[lang] if isinstance(value[lang], str) else tuple(value[lang])
                for key, value in raw_controls.items()
            }
            dictionary['readme'] = open(f"{directory}/readme_page_{lang}.txt").read()
            logger.info(f'dizionario : {dictionary}')

        else:
            dictionary = {
                value["label"][lang]: value["description"][lang]
                for value in raw_controls.values()
            }
        return dictionary
    
    except Exception as e:
        logger.error(f"Errore nel caricamento del file json {file_json}: {e}")
        return ""

# ----- Translations -----  
def load_translations(language: str = "en") -> dict:
    """Load translations from JSON file"""
    file_path = Path(f"config/translations/{language}.json")
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        st.write(f"Unable to find translation file for language {language}")
    return {}