import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

datasets=pd.read_csv("cs-training.csv",index_col=0)
datasets=datasets.dropna()

datasets2=pd.read_csv("cs-test.csv",index_col=0)
datasets2=datasets2.dropna()
#print(datasets.isna().sum())
train_labels=datasets["SeriousDlqin2yrs"]
train_data=datasets.drop(["SeriousDlqin2yrs"],axis=1)

test_labels=datasets["SeriousDlqin2yrs"]
test_data=datasets.drop(["SeriousDlqin2yrs"],axis=1)

data1=train_data[:20000]
data1_labels=train_labels[:20000]
data2=train_data[20000:40000]
data2_labels=train_labels[20000:40000]
data3=train_data[40000:60000]
data3_labels=train_labels[40000:60000]
data4=train_data[60000:80000]
data4_labels=train_labels[60000:80000]
data5=train_data[80000:100000]
data5_labels=train_labels[80000:100000]
data6=train_data[100000:120269]
data6_labels=train_labels[100000:120269]

rfc2 = RandomForestClassifier(n_estimators=100, max_depth=50,
                              random_state=0)
rfc2.fit(data2, data2_labels)
preds1=rfc2.predict(test_data)
pr = accuracy_score(test_labels, preds1)
pr=pr*100

print(pr)

joblib.dump(rfc2,'model2.pkl')
