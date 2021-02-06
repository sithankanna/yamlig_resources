import os
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler

class EDA:
    def __init__(self, root_path: str) -> None:
        self.root_path = root_path

    def load(self, file_name: str) -> pd.DataFrame:
        if file_name is not None:
            df = pd.read_csv(os.path.join(self.root_path, file_name))
            return df
        else: 
            print("No file to read")
