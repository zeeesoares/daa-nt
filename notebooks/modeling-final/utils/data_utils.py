import pandas as pd
from . import TRAIN_PATH, TEST_PATH

def load_datasets():
    train = pd.read_csv(TRAIN_PATH, encoding='latin1')
    test = pd.read_csv(TEST_PATH, encoding='latin1')
    return train, test