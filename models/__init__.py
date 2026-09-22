"""
Пакет с классами предметной области.
"""

from .residents import Resident
from .requests import Request
from .premises import Premise
from .services import Service

__all__ = ["Resident", "Request", "Premise", "Service"]
