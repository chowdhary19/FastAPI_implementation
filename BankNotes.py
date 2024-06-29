# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020
"""

from pydantic import BaseModel

# Class to describe the measurements of bank notes
class BankNoteData(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
