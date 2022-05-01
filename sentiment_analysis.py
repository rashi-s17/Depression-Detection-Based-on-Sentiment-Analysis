import json
import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import naive_bayes

from algorithms import naive_bayes, decision_tree, support_vector_machine, k_neighbours_classifier, random_forest

tweets_data = []
x = []
y = []
vectorizer = CountVectorizer(stop_words='english')

def retrieveTweet(data_url):

    tweets_data_path = data_url
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

             
def retrieveProcessedData(Pdata_url):
    sent = pd.read_excel(Pdata_url)
    for i in range(len(tweets_data)):
        if tweets_data[i]['id']==sent['id'][i]:
            x.append(tweets_data[i]['text'])
            y.append(sent['sentiment'][i])

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')          


def runall():     
    retrieveTweet('data/tweetdata.txt')  
    retrieveProcessedData('processed_data/output.xlsx')
    naive_bayes.nbTrain(x, y)
    decision_tree.datree(x, y)
    support_vector_machine.Tsvm(x, y)
    k_neighbours_classifier.knn(x, y)
    random_forest.randomForest(x, y)
    
def datreeINPUT(inputtweet):
    from sklearn import tree
    train_featurestree = vectorizer.fit_transform(x)
    dtree = tree.DecisionTreeClassifier()
    
    dtree = dtree.fit(train_featurestree, [int(r) for r in y])
    
    
    inputdtree= vectorizer.transform([inputtweet])
    predictt = dtree.predict(inputdtree)
    
    if predictt == 1:
        predictt = "Positive"
    elif predictt == 0:
        predictt = "Neutral"
    elif predictt == -1:
        predictt = "Negative"
    else:
        print("Nothing")
    
    print("\n*****************")
    print(predictt)
    print("*****************")

runall()

print("Input your tweet : ")
inputtweet = input()

datreeINPUT(inputtweet)
