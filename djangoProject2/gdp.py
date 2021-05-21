import sys

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from pyearth import Earth
import joblib
y_s = 0
y_s = sys.argv[1];
n=y_s
ans =0
for i in range(len(n)):
    if n[i].isnumeric():
            ans = ans + int(n[i])*pow(10,(len(n)-1)-i)
gdpdata = pd.read_csv("/home/cheeryluck/PycharmProjects/djangoProject2/data1/IndiaGDP.csv", header=None)
labels = ['Year', 'GDP']
gdpdata.columns = labels


train, test = train_test_split(gdpdata)

model6 = Earth().fit(train.iloc[:, :1], train.iloc[:, 1:])
ycap6 = model6.predict(test.iloc[:, :1])

error = mean_squared_error(test.iloc[:, :1], ycap6)

model6.predict([[2019]])
joblib.dump(model6,'/home/cheeryluck/PycharmProjects/djangoProject2/data1/GDP_Model.sav')
impmodel=joblib.load('/home/cheeryluck/PycharmProjects/djangoProject2/data1/GDP_Model.sav')

print(impmodel.predict([[2019]]))
