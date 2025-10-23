import streamlit as st
import pandas as pd

class DataManager():
    def __init__(self):
        self.df = pd.DataFrame()