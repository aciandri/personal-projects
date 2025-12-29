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