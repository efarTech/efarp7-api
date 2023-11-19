from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

import os

from datetime import datetime, date

import pandas as pd
import numpy as np

import joblib
import warnings
import dill
import logging

from flask import Flask

class EfarScoringController:
    """
    Efardb class
    """
    def __init__(self, repository):
        """
        __init__ method
        """
        self.df_scoring = repository.get_scoring()
    
    def get_scoring(self):
        """
        get_scoring method
        """
        return self.df_scoring
        