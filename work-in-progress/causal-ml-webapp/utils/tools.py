# ----- Libraries -----
import json

from log_config import get_logger

# ----- Logging -----
logger = get_logger(__name__)

# ----- Get JSON files -----
def load_json(flag_ita: bool, 
              file_json: str,
              directory: str = "texts/") -> dict:
    """ 
    Carica il file JSON e ne estrae un dizionario.
    Le modalità di conversione dipendono dal file: texts sono le parti testuali della webapp, mentre controls sono i controlli di dataquality da effettuare.

    Args:
        flag_ita (bool): True se la lingua è impostata a "Italiano".
        file_json (str): Nome del file json senza estenzione e senza directory.

    Returns:
        Dizionario con i controlli da effettuare o i readme.
    """

    try:
        with open(f"{directory + file_json}.json", "r", encoding="utf-8") as f:
            raw_controls = json.load(f)
        lang = "ita" if flag_ita else "eng"

        if file_json == 'texts':
            dictionary = {
                key: value[lang] if isinstance(value[lang], str) else tuple(value[lang])
                for key, value in raw_controls.items()
            }
            dictionary['readme'] = open(f"{directory}/readme_{lang}.txt").read()
        else:
            dictionary = {
                value["label"][lang]: value["description"][lang]
                for value in raw_controls.values()
            }

        return dictionary
    
    except Exception as e:
        logger.error(f"Errore nel caricamento del file json {file_json}: {e}")
        return ""