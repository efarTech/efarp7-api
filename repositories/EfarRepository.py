from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

import os

from datetime import datetime, date

import pandas as pd
import numpy as np

import warnings
import joblib
import logging
import pickle5 as pickle

from modules.file.EfarDataFile import EfarDataFile

class EfarRepository:
    """
    Efardb class
    """
    def __init__(self, directory):
        """
        __init__ method
        """
        self.efardatafile=EfarDataFile(directory)
        self.df_scoring, self.customers_references, self.lightgbm_model = self.load_data(directory)
    
    def load_data(self, directory):
        df_scoring = self.efardatafile.to_data('data_api', 'scr')
        df_scoring = df_scoring.set_index('SK_ID_CURR')
        customers_references = df_scoring.index.unique()
        
        #with open(f'{directory}/lightgbm.pickle') as f:
        #    lightgbm_model = pickle.load(f)
        
        lightgbm_model = joblib.load(f'{directory}/lightgbm_model.joblib')
        
        return df_scoring, customers_references, lightgbm_model
    
    def get_customers_references(self):
        """
        get_customers_references method
        """
        return self.customers_references
             
    def get_scoring(self):
        """
        get_scoring method
        """
        return self.df_scoring
            
    def get_model(self):
        """
        get_model method
        """
        return self.lightgbm_model
   
