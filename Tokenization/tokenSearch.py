# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 19:30:36 2017

@author: Omar
"""
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score



import numpy as np

from itertools import product

from sklearn.ensemble import RandomForestClassifier


def tokenSearch(playsFrame): 
    
    vecDict = {}
    vectorizers = ["CountVectorizer","TfidfVectorizer"]
    stopWords= [None, "english"]
    grams = [1,2,3]
    maxDF = [0.7,0.8,0.9,1.0]
    
    labeler = LabelEncoder()
    y = labeler.fit_transform(playsFrame.Play)

    for params in product(vectorizers,stopWords,grams, maxDF):
        print params
        if params[0] == "CountVectorizer":
            vectorizer = CountVectorizer(stop_words = params[1],ngram_range = (0,params[2]),max_df = params[3])
        else:
            vectorizer = CountVectorizer(stop_words = params[1],ngram_range = (0,params[2]),max_df = params[3])
        
        X = vectorizer.fit_transform(playsFrame.Speech)
    
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        
        forest = RandomForestClassifier(n_estimators = 100,n_jobs = 7) 
        forest = forest.fit( X_train, y_train)
        result = forest.predict(X_test)
        f1 =f1_score(y_test,result,average = 'micro')
        
        vecDict[params] = f1
        
    return vecDict

vecDict = tokenSearch(playsFrame)
vecDF = pd.DataFrame().from_dict(vecDict,orient = 'index')

vecDF.rename(columns = {0:"f1_score"},inplace = True)
vecDF.column = ["f1_score"]
vecDF = vecDF.set_index(pd.MultiIndex.from_tuples(vecDF.index,
                                                  names = ('vectorizer','stopwords','grams','maxDF'))).sort_index()

bestPerformingTokenizer = vecDF.idxmax()