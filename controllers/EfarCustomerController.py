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

from flask import Flask, jsonify
from repositories.EfarRepository import EfarRepository

class EfarCustomerController:
    """
    Efardb class
    """
    def __init__(self, directory):
        """
        __init__ method
        """
        self.repository = EfarRepository(directory)
        self.customers_references = self.repository.get_customers_references()
    
    def get_customers_references(self):
        """
        get_customers_references method
        """
        return jsonify(
            {
                'model': 'lightgbm',
                'customers_references' : list(self.customers_references.astype(str))
            }
        )
        