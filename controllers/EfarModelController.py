from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

import os

from datetime import datetime, date

import pandas as pd
import numpy as np

import warnings
import dill
import logging

from flask import Flask
from repositories.EfarRepository import EfarRepository

class EfarModelController:
    """
    Efardb class
    """
    def __init__(self, directory):
        """
        __init__ method
        """
        self.repository = EfarRepository(directory)
        self.lightgbm_model = self.repository.get_model()
    
    def get_model(self):
        """
        get_model method
        """
        return self.lightgbm_model
        