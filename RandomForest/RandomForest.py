# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 22:39:34 2017

@author: Omar
"""


from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators = 100,n_jobs = 7) 

# Fit the forest to the training set, using the bag of words as 
# features and the sentiment labels as the response variable
#
# This may take a few minutes to run
forest = forest.fit( X_train, y_train)

from sklearn.metrics import confusion_matrix

result = forest.predict(X_test)
cm = confusion_matrix(labeler.inverse_transform(y_test),labeler.inverse_transform(result))



import matplotlib.pyplot as plt

labels = list(labeler.classes_)
fig = plt.figure(figsize=(8, 6),dpi=80)
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
plt.title("CM")
fig.colorbar(cax)
if labels:
    ax.set_xticklabels([''] + labels)
    ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

from sklearn.metrics import accuracy_score

from sklearn.metrics import f1_score

print f1_score(y_test,result,average = 'micro')

########################
# forest = RandomForestClassifier(n_estimators = 100,n_jobs = 7) 
# count, no stopwords, no grams, stock RF F1 score: 0.28332518337408313
# count, english stopwords, no grams 0.28391198044
# count, no stopwords, trigrams 0.294180929095
# count, english stopwords, trigrams 0.310024449878

# tf idf, no stopwords, no grams 0.301515892421
# tf idf, english stopwords, no grams 0.31413202934
# tf idf, no stopwords, trigrams 0.293007334963
# tf idf, english stopwords, trigrams 0.309437652812

# check if its just recognizing names!
