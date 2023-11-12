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

class EfarScoringController:
    """
    Efardb class
    """
    def __init__(self, directory):
        """
        __init__ method
        """
        self.repository = EfarRepository(directory)
        self.df_scoring = self.repository.get_scoring()
    
    def get_scoring(self):
        """
        get_scoring method
        """
        return self.df_scoring
        