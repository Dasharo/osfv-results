import pandas as pd
import sys
import os

# Modify the models list to match the file structure
models = [
    "V54x_MTL V54x_MTL v0.9.0-rc2",
    "V54xNx_MTL V54xNx_MTL v0.9.0-rc2"
    ]

file_path = os.path.abspath(os.path.dirname(__file__))
in_file = file_path + "/../../../results.csv"
out_file = file_path + "/results.csv"

data = pd.read_csv(in_file, sep=",")

columns = ["Test name", "Test ID"]
columns.extend(models)

selected = data[columns]

selected.to_csv(out_file, index=False)
