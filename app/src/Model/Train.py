import csv
import joblib
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

CORRESP_LANG = [
    "FR",
    "EN-GB",
    "IT",
    "ES",
    "PT-PT",
    "DE"
]

def read_data(test_size=0.2):
    x, y = [], []
    #TO DO boucler sur toutes les langues
    i = 1
    for lang in CORRESP_LANG:
        first = True
        with open("../../assets/data/trainset/"+lang+"_trainset.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if first != True:
                    x.append(np.array(row, dtype = np.float64))
                    y.append(i)
                else:
                    first = False
        i += 1
    print(np.array(x))
    return train_test_split(np.array(x), y, test_size=test_size, random_state=5)

def train(test_size):
    x_train, x_test, y_train, y_test = read_data(test_size=test_size)
    print("Nombre de données d'entrainement : " + str(x_train.shape[0]))

    model = SGDClassifier()
    model.fit(x_train, y_train)
    joblib.dump(model, "model.sav")

    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
    print("Accuracy: {:.2f}%".format(accuracy * 100))

    # return np.array(x), y

train(0.2)