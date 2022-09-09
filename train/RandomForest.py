import sys
from urllib.parse import urlparse
# import mlflow
from matplotlib import pyplot as plt

# import mlflow
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import ElasticNet, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.ensemble import RandomForestRegressor

import numpy as np
import pandas as pd
import seaborn as sns
import sys
import warnings
import os

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../scripts')))
sys.path.append(os.path.abspath(os.path.join('../scripts')))
from plot_data import PlotData

# Initialize Plot
plot = PlotData()


data = pd.read_csv('data2/train_cleaned.csv', sep=',')
data.drop(['Unnamed: 0'], axis=1, inplace=True)
data.set_index('Date', inplace=True)

data.drop(['StateHoliday'], axis=1, inplace=True)

data = data[data['Open'] == 1]
data = data[data['Sales'] > 0.0]

X = data.drop('Sales', axis=1)
y = data['Sales']
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=123)

regr = RandomForestRegressor(max_depth=2, random_state=123)
regr.fit(X_train, y_train)
    
train_score = regr.score(X_train, y_train) * 100
test_score = regr.score(X_test, y_test) * 100
    
    #write scores to file
with open("train/metrics.txt", 'w') as outfile:
    outfile.write(f"Validation data accuracy: {train_score}")
    outfile.write(f"Test varianc: {test_score}")
        
 #calculate feature importance
    
importances = regr.feature_importances_
labels = df.columns
feature_df = pd.DataFrame(list(zip(labels, importances)), columns = ["feature","importance"])
feature_df = feature_df.sort_values(by='importance', ascending=False,)

# image formatting
axis_fs = 18 #fontsize
title_fs = 22 #fontsize
sns.set(style="whitegrid")

ax = sns.barplot(x="importance", y="feature", data=feature_df)
ax.set_xlabel('Importance',fontsize = axis_fs) 
ax.set_ylabel('Feature', fontsize = axis_fs)#ylabel
ax.set_title('Random forest\nfeature importance', fontsize = title_fs)

plt.tight_layout()
plt.savefig("feature_importance.png",dpi=120) 
plt.close()


##########################################
############ PLOT RESIDUALS  #############
##########################################

y_pred = regr.predict(X_test) + np.random.normal(0,0.25,len(y_test))
y_jitter = y_test + np.random.normal(0,0.25,len(y_test))
res_df = pd.DataFrame(list(zip(y_jitter,y_pred)), columns = ["true","pred"])

ax = sns.scatterplot(x="true", y="pred",data=res_df)
ax.set_aspect('equal')
ax.set_xlabel('True wine quality',fontsize = axis_fs) 
ax.set_ylabel('Predicted wine quality', fontsize = axis_fs)#ylabel
ax.set_title('Residuals', fontsize = title_fs)

# Make it pretty- square aspect ratio
ax.plot([1, 10], [1, 10], 'black', linewidth=1)
plt.ylim((2.5,8.5))
plt.xlim((2.5,8.5))

plt.tight_layout()
plt.savefig("residuals.png",dpi=120) 
