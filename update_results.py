#!/usr/bin/env python3


import pandas as pd
import os
import os.path


BOARDS_PATH = os.path.abspath(os.path.dirname(__file__)) + "/boards/"
MATRIX_URL = r"https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/export?format=csv&gid=736501945#gid=736501945"
RESULTS_FILENAME = "results.csv"
EMPTY_RESULT_VALUES = [
    "Not Tested",
    "NOT TESTED",
    "Skip",
    "SKIP", 
    "BLANK",
    "NaN",
    ""
]
IGNORE_FLAG_FILENAME = "manual_update"
IGNORE_BOARDS = [
    "ms7d25",
    "ms7e06"
]


def should_be_dropped(row):
    return all(x in EMPTY_RESULT_VALUES for x in row)


def update_results_there(filename: str):
    data: pd.DataFrame = pd.read_csv(filename)
    # Update only the columns which already exist in the results.csv file
    columns = data.columns
    selected = data_from_matrix[columns]

    # Create a mask, 1 if should be dropped, 0 otherwise
    # Skipping two first columns
    mask = selected.iloc[:, 2:].apply(should_be_dropped, axis=1)

    # Filter using the mask
    selected = selected[~mask]

    selected.to_csv(filename, index=0)


# Download the Matrix
print("-- Downloading: " + MATRIX_URL)
data_from_matrix: pd.DataFrame = pd.read_csv(MATRIX_URL, skiprows=[0])

# Find vendor directories in file structure
vendors = [os.path.join(BOARDS_PATH, d) for d in os.listdir(BOARDS_PATH)]

# Find model families of each vendor
models = []
for v in vendors:
    models.append([os.path.join(v, m) for m in os.listdir(v)])
models = sum(models, [])

# Skip directories containing IGNORE_FLAG_FILENAME file or
# included in IGNORE_BOARDS list
# if such behaviour is needed
models = [m for m in models if 
            (not os.path.isfile(os.path.join(m, IGNORE_FLAG_FILENAME))) 
            and 
            (not os.path.basename(m) in IGNORE_BOARDS)
        ]

# Find results.csv files in model family directories
tables = [os.path.join(m, RESULTS_FILENAME) for m in models]
tables = [t for t in tables if os.path.isfile(t)]

# Update results.csv files
for table in tables:
    print("-- Updating: " + table)
    update_results_there(table)

print ("-- Done.")
