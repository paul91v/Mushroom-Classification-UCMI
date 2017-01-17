# -*- coding: utf-8 -*-

import pandas as pd
import settings

RawData = pd.read_csv(settings.RAW_FILE)
Train = RawData.sample(frac = 0.7, random_state = 101)
Test = RawData.drop(Train.index)
Train.to_csv(str(settings.PROCESSED_DIR + "\Train.csv"), index = False)
Test.to_csv(str(settings.PROCESSED_DIR + "\Test.csv"), index = False)