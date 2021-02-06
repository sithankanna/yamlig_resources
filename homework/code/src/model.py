import pandas as pd
import numpy as np
import os
from typing import Set, Dict, List

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

class Model:
    def __init__(self, features: List[str]) -> None:
        self.features = features
        self.features = len(features)

    def train(self):
        pass

    def predict(self):
        pass