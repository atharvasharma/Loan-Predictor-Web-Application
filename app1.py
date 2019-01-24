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

rfc = RandomForestClassifier(n_estimators=100, max_depth=50,
                              random_state=0)
rfc.fit(data1, data1_labels)
preds1=rfc.predict(test_data)
pr = accuracy_score(test_labels, preds1)
pr=pr*100

print(pr)

joblib.dump(rfc,'model1.pkl')

joblib.dump(data1,"data1.pkl")
joblib.dump(data1_labels,"data_labels1.pkl")

joblib.dump(data2,"data2.pkl")
joblib.dump(data2_labels,"data_labels2.pkl")

joblib.dump(data3,"data3.pkl")
joblib.dump(data3_labels,"data_labels3.pkl")

joblib.dump(data4,"data4.pkl")
joblib.dump(data4_labels,"data_labels4.pkl")

joblib.dump(data5,"data5.pkl")
joblib.dump(data5_labels,"data_labels5.pkl")

joblib.dump(data6,"data6.pkl")
joblib.dump(data6_labels,"data_labels6.pkl")

