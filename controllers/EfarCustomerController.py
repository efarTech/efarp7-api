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

class EfarCustomerController:
    """
    Efardb class
    """
    def __init__(self, repository):
        """
        __init__ method
        """
        self.customers_references = repository.get_customers_references()
    
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
        