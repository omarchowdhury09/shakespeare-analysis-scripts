# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 14:40:51 2017

@author: Omar
"""

# Optimal Tokenizer Params
# (TfidfVectorizer, english, 2, 1.0)
# F1 score of ~.317 (~2% on 37 classes)

vectorizer = TfidfVectorizer(stop_words = 'english',ngram_range = (0,2),max_df = 1.0)
X = vectorizer.fit_transform(playsFrame.Speech)

labeler = LabelEncoder()
y = labeler.fit_transform(playsFrame.Play)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators = 100,n_jobs = 7) 
forest = forest.fit( X_train, y_train)

from sklearn.metrics import confusion_matrix

result = forest.predict(X_test)
cm = confusion_matrix(labeler.inverse_transform(y_test),labeler.inverse_transform(result))


print f1_score(y_test,result,average = 'micro')

lowerNames = playsFrame.Character.str.lower().unique()

vocab = vectorizer.get_feature_names()

namePos = {}
# 619 of 928 names found
for name in lowerNames:
    try:
        pos = vocab.index(name)
        namePos[name] = pos
    except ValueError:
        print "%s not found" % (name,)

nameIndices = namePos.values()

classifiedCorrectly = np.where(result - y_test == 0)[0]
xClass =  X_test[classifiedCorrectly,:]

from scipy.sparse import find
correctNameDict = {}
for i in range(0,xClass.shape[0]):
    thisLine = xClass[i,:]
    wordIndices = find(xClass[i,:])[1]
    
    correctNameDict[i] = np.intersect1d(wordIndices,nameIndices)

correctCt = 0
for val in correctNameDict:
    if len(correctNameDict[val]) > 0:
        print correctNameDict[val]
        correctCt = correctCt + 1
        
# about 65% of correctly classified lines contain a name

lineDict = {}
for i in range(0,X_test.shape[0]):
    wordIndices = find(X_test[i,:])[1]
    
    lineDict[i] = np.intersect1d(wordIndices,nameIndices)
 
ct = 0
for val in lineDict:
    if len(lineDict[val]) > 0:
        # print correctNameDict[val]
        ct = ct + 1

# about 43% of all lines in test set contain a name
# ...awkward