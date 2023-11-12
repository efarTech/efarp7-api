from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

import sys
import os

#sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from repositories.EfarRepository import EfarRepository

class TestEfarRepository:
    def test_when_get_customers_references(self):
        """
        test_when_get_customers_references method
        """
        repository = EfarRepository('../repositories/data/')
        assert len(repository.get_customers_references()) > 0
            
    def test_when_get_scoring(self):
        """
        test_when_get_scoring method
        """
        repository = EfarRepository('../repositories/data/')
        assert repository.get_scoring() is not None
            
    def test_get_model(self):
        """
        test_get_model method
        """
        repository = EfarRepository('../repositories/data/')
        assert repository.get_model() is not None