import pandas as pd
import os
import os.path

pwd = os.path.abspath(os.path.dirname(__file__))
results_path = pwd + "/results.csv"
boards_path = pwd + "/boards/"
matrix_url = r"https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/export?format=csv&gid=736501945#gid=736501945"


print("-- Downloading: " + matrix_url)
data = pd.read_csv(matrix_url, skiprows=[0])
data.to_csv(results_path)

vendors = [os.path.join(boards_path, d) for d in os.listdir(boards_path)]
models = []
for v in vendors:
    models.append([os.path.join(v, m) for m in os.listdir(v)])
models = sum(models, [])

scripts = [os.path.join(m, "update_results.py") for m in models]
scripts = [s for s in scripts if os.path.isfile(s)]

for script in scripts:
    print("-- Updating: " + script)
    os.system("python3 " + script)

print("-- Cleaning...")
os.remove(results_path)
