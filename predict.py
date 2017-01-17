# -*- coding: utf-8 -*-

import settings
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics, cross_validation
from sklearn.preprocessing import LabelEncoder

def PreProcess(Train):
    prep = LabelEncoder()
    for col in Train[settings.PREDICTORS].columns:
        Train[col] = prep.fit_transform(Train[col])
    return Train

def cross_validate_RF(train, CV_FOLDS):
    footy_RF = RandomForestClassifier(n_jobs = -1)
    predictions = cross_validation.cross_val_predict(footy_RF, train[settings.PREDICTORS], train[settings.TARGET], cv = CV_FOLDS)
    return predictions
    
def GridCV(Train, classifier):
    errors = []
    errors.append(0)
    errors.append(0)
    for i in range(2,21):
        predictions = cross_validation.cross_val_predict(classifier(), Train[settings.PREDICTORS], Train[settings.TARGET], cv = i)
        errors.append(metrics.accuracy_score(Train[settings.TARGET], predictions))
    return errors
    
if __name__ == "__main__":
    Train = pd.read_csv(settings.PROCESSED_DIR + "\Train.csv")
    Train = PreProcess(Train)
    #CV_FOLDS = GridCV(Train, RandomForestClassifier)
    predictions_rf = cross_validate_RF(Train, settings.CV_FOLDS)
    error_rf = metrics.accuracy_score(Train[settings.TARGET], predictions_rf)
    print('CV-RF Training Accuracy Score: {}'.format(round(error_rf,4)))
    