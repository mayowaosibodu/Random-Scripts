# Script to parse a malware dataset, train a Random Forest DecisionTreeClassifier
# on the data, and print out a list of the most important features for classification.


import pandas as pd


data = pd.read_csv('~/Files/z hpd/pe-files-malwares/dataset_malwares.csv')

columns = (data.columns)
print( "Total dataset: ", len(data))

X = data.drop('Name', axis= 1)

malware = data[data['Name'].str.startswith('VirusShare')]
print ("Malware: ", len(malware))

goodware = data[data['Name'].str.startswith('VirusShare')== False]
print ("Goodware: ", len(goodware))

Y = [1]*len(malware) + [0]*len(goodware)


from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

# clf = tree.DecisionTreeClassifier()
clf = RandomForestClassifier(n_estimators=10)

clf.fit(X, Y)

importance = (clf.feature_importances_)
importances = []

print ('\n \n')
for i in range(len(importance)):
    importances.append( (columns[i], importance[i]) )

importances = sorted(importances, key= lambda imp:imp[1])
importances.reverse()

for i in importances:
    print (i)



Y_ = clf.predict(X)

from sklearn.metrics import accuracy_score

print ('\n \n Accuracy of Model on the training set is:', accuracy_score(Y, Y_))
