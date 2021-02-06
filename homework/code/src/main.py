import os
import pandas as pd
import numpy as np

from model import Model
from eda import EDA

P_INPUT = "data"
P_OUTPUT = "output"

def run() -> None:
    eda = EDA(root_path=P_INPUT)
    df = eda.load(file_name=None)
    print("hello world")

    pass


if __name__ == "__main__":
    run()