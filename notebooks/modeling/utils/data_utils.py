import pandas as pd
from . import TRAIN_PATH, TEST_PATH

def load_datasets():
    train = pd.read_csv(TRAIN_PATH, keep_default_na=False)
    test = pd.read_csv(TEST_PATH, keep_default_na=False)
    return train, test
