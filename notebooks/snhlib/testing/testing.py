import os

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from snhlib.multitools import evaluate_clf
from snhlib.multitools import FindData

from snhlib.dataviz import CalcPCA

print(os.getcwd())

data = pd.read_csv("snhlib/testing/iris.csv")
ind = data.variety.isin(["Virginica", "Versicolor"])
data = data[ind].reset_index(drop=True)

# trial evaluate_clf
model = LogisticRegression()
scaler = StandardScaler()
X, y = data.values[:, :-1], data.values[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y)

evaluate_clf(
    model, X_train, X_test, y_train, y_test, scaler=scaler, pos_label=["Virginica", "Versicolor"]
)


pca = CalcPCA()
pca.fit(X, y)
pca.plotpc()


# trial FindData
path_ = "/Users/shidiq/Developer/examples"
list_data = FindData(path=path_)
list_data.get_files
list_data.get_files_swap
