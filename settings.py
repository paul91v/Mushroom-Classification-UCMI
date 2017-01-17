# -*- coding: utf-8 -*-

RAW_FILE = 'C:\Anaconda3\Workspace\Mushroom-Classification\Data\mushrooms.csv'
PREDICTORS = [ 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat']
TARGET = 'class'
CV_FOLDS = 5
DATA_DIR = "C:\Anaconda3\Workspace\Mushroom-Classification\Data"
PROCESSED_DIR = "C:\Anaconda3\Workspace\Mushroom-Classification\Processed"