"""
Contained in file are functions used for
    - training scikit learn classifiers
    - making prediction with each algorithm

Import your classifier and add respective lines
"""
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.model_selection import cross_val_score, StratifiedShuffleSplit
from sklearn.neural_network import MLPClassifier

RAND_STATE = 0
TEST_SIZE = 0.1
NUMBER_OF_SPLITS = 100
SCORING_METHOD = 'accuracy'


def train_classifier(data, labels, classifier, **kwargs):
    model = classifier(**kwargs)
    cv = StratifiedShuffleSplit(
        n_splits=NUMBER_OF_SPLITS,
        test_size=TEST_SIZE,
        random_state=RAND_STATE
    )
    scores = cross_val_score(model, data, labels, cv=cv, scoring=SCORING_METHOD)
    print( sum(scores) / len(scores))
    score = sum(scores) / len(scores)
    return model.fit(data, labels), score


def train_nc(data,labels,**kwargs):
    return train_classifier(data,labels, NearestCentroid,**kwargs)


def train_mlp(data, labels):
    return train_classifier(data, labels, MLPClassifier, max_iter=300, solver='sgd')


def make_test_prediction(model, data, labels, print_details=True):
    pred = model.predict(data)
    probs = model.predict_proba(data)
    print('Predictions:', pred)
    print('Probabilies:', probs)
    # if print_details:
    #     print('score', accuracy_score(pred, labels))
    #     print('pred', pred)
    #     print('actual', labels)
    #     print(confusion_matrix(labels,pred))

    return pred


def get_prediction_and_prob(model, data):
    pred = model.predict(data)
    probs = model.predict_proba(data)
    return pred, probs

