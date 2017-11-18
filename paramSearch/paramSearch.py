# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 19:30:36 2017

@author: Omar
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import numpy as np


from sklearn.ensemble import RandomForestClassifier

def paramSearch():
    vectorizers = ["CountVectorizer","TfidfVectorizer"]
    stopWords= [None, "english"]
    grams = [1,2,3]
    maxDF = [0.7,0.8,0.9,1.0]
    
    