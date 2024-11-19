#%%

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import roc_auc_score
# loading libraries
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
import pickle

df = pd.read_csv('bank-additional-full.csv', sep=';')

df.y = (df.y == 'yes').astype(int)

columns = []
for c in list(df.columns):
    columns.append(c.replace('.','_'))

categorical_features = list(df.dtypes[df.dtypes == 'object'].index)
categorical_features

numerical_features = list(df.dtypes[df.dtypes != 'object'].index)
numerical_features.remove('y') # let us remove the target column of the dataset


df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train.y.values
y_test = df_test.y.values

del df_full_train['y']
del df_test['y']

del df_test['duration']
del df_full_train['duration']

#%%

full_train_dict = df_full_train.to_dict(orient='records')
test_dict = df_test.to_dict(orient='records')

dv = DictVectorizer(sparse=False)

X_full_train = dv.fit_transform(full_train_dict)
X_test = dv.transform(test_dict)

#%%

features = list(dv.get_feature_names_out())

#%%
dfulltrain = xgb.DMatrix(X_full_train, label=y_full_train, feature_names=features)
dtest = xgb.DMatrix(X_test, label=y_test, feature_names=features)

xgb_params = {
    'eta': 0.05,
    'max_depth': 6,
    'min_child_weight': 1,

    'objective': 'binary:logistic',
    'nthread': 8,
    'eval_metric': 'auc',

    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dfulltrain, num_boost_round=120)
y_pred = model.predict(dtest)
print(roc_auc_score(y_test, y_pred))


output_filename = 'model.bin'
f_out = open(output_filename, 'wb') # w is for write and b is for binary
pickle.dump((dv, model), f_out)
f_out.close()