# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 22:25:59 2017

@author: Omar
"""


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import numpy as np

######################################################

#############
# TODO: Try decreasing max_df
    
# vectorizer = CountVectorizer(stop_words = 'english',ngram_range = (0,3))

vectorizer = TfidfVectorizer(stop_words = 'english',ngram_range = (0,3))

X = vectorizer.fit_transform(playsFrame.Speech)
# X = transformer.fit_transform(playsFrame.Speech)

# vocab = vectorizer.get_feature_names()

# dist = np.sum(X.toarray(), axis = 0)
# xList = list( X[i,:].toarray() for i in range(0,X.shape[0]))

labeler = LabelEncoder()
y = labeler.fit_transform(playsFrame.Play)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

frequencyTable = pd.DataFrame(zip(vocab,dist),columns = ["Word","Frequency"])

frequencyTable.sort_values("Frequency",
                           ascending = False).head(50).plot(x="Word",
                                                  y="Frequency",kind= 'bar')


