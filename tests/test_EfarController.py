from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

import sys
import os

#sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from flask import Flask
from controllers.EfarCustomerController import EfarCustomerController
from controllers.EfarScoringController import EfarScoringController
from controllers.EfarModelController import EfarModelController

class TestEfarController:
    def test_when_get_customers_references_from_controller(self):
        """
        test_when_get_customers_references method
        """
        app = Flask(__name__)
        
        with app.app_context():
            customerController = EfarCustomerController('../repositories/data/')
            assert customerController.get_customers_references() is not None
            
    def test_when_get_scoring_from_controller(self):
        """
        test_when_get_scoring method
        """
        scoringController = EfarScoringController('../repositories/data/')
        assert scoringController.get_scoring() is not None
            
    def test_get_model_from_controller(self):
        """
        test_get_model method
        """
        modelController = EfarModelController('../repositories/data/')
        assert modelController.get_model() is not None