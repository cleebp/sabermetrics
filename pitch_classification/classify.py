"""
classify.py

@author: Brian Clee
@date: 1/19/18

@purpose: Take 'train.csv' and 'test.csv' and classify the pitch types using KNN w/a variety of features.
@requirements: Python3.4, pandas, numpy, sklearn, scipy
@arguments: train.csv and test.csv
"""

# imports
import sys
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# implement KNN algorithm for combinations of horizontal movement, vertical movement, and start speed
def knn(train_file, test_file):
    data = pd.read_csv(train_file, header=0)
    #test = pd.read_csv(test_file, header=0)

    # predict and score for horizontal movement [10] and vertical movement [11]
    # first subset the data
    X = np.array(data.ix[:, 10:12])  # x0 .. pfx_z
    label = np.array(data['pitch_type'])
    X_train, X_test, label_train, label_test = train_test_split(X, label, test_size=0.33, random_state=42)

    # next setup KNN, fit, predict, and evaluate accuracy
    knn = KNeighborsClassifier(n_neighbors=10)
    knn.fit(X_train, label_train)
    pred = knn.predict(X_test)
    HV_score = accuracy_score(label_test, pred)

    # predict and score for start speed [5] and vertical movement [11]
    # first subset the data
    X = np.array(data.ix[:, [5,11]])
    X_train, X_test, label_train, label_test = train_test_split(X, label, test_size=0.33, random_state=42)

    # next setup KNN, fit, predict, and evaluate accuracy
    knn.fit(X_train, label_train)
    pred = knn.predict(X_test)
    SV_score = accuracy_score(label_test, pred)

    # predict and score for start speed [5] and horizontal movement [10]
    # first subset the data
    X = np.array(data.ix[:, [5, 10]])
    X_train, X_test, label_train, label_test = train_test_split(X, label, test_size=0.33, random_state=42)

    # next setup KNN, fit, predict, and evaluate accuracy
    knn.fit(X_train, label_train)
    pred = knn.predict(X_test)
    HS_score = accuracy_score(label_test, pred)

    print("\nAccuracy values...\n")
    print("Using horizontal movement and vertical movement:")
    print(str(HV_score) + "\n")
    print("Using start speed and vertical movement:")
    print(str(SV_score) + "\n")
    print("Using horizontal movement and start speed:")
    print(str(HS_score) + "\n")

# implement KNN for all combinations of possible feature pairs, display the strongest results
def feature_explore(train_file, test_file):
    data = pd.read_csv(train_file, header=0)
    label = np.array(data['pitch_type'])
    knn = KNeighborsClassifier(n_neighbors=10)

    print("Beginning feature exploration...\n")
    # dont worry about descriptive features
    exclude = [12, 13, 14, 15]
    for i in range(5, 22):
        if i in exclude:
            continue
        for j in range(i, 22):
            if j in exclude:
                continue
            X = np.array(data.ix[:, [i, j]])
            X_train, X_test, label_train, label_test = train_test_split(X, label, test_size=0.33, random_state=42)

            knn.fit(X_train, label_train)
            pred = knn.predict(X_test)
            score = accuracy_score(label_test, pred)

            # only print out the most accurate results
            if score > 0.64:
                print("With features " + str(i) + " and " + str(j) + " accuracy score:")
                print(str(score) + "\n")

def main():
    if len(sys.argv) is not 3:
        print("Error. Please run this script with train.csv and test.csv as arguments:")
        print("python3 classify.py train.csv test.csv")
        sys.exit(0)

    train_file = sys.argv[1]
    test_file = sys.argv[2]

    knn(train_file, test_file)

    feature_explore(train_file, test_file)

main()