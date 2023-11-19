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

class EfarModelController:
    """
    Efardb class
    """
    def __init__(self, repository):
        """
        __init__ method
        """
        self.lightgbm_model = repository.get_model()
    
    def get_model(self):
        """
        get_model method
        """
        return self.lightgbm_model
        