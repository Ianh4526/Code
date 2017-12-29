import pandas as pd

feature_names =  ['party','handicapped-infants', 'water-project-cost-sharing',
                    'adoption-of-the-budget-resolution', 'physician-fee-freeze',
                    'el-salvador-aid', 'religious-groups-in-schools',
                    'anti-satellite-test-ban', 'aid-to-nicaraguan-contras',
                    'mx-missle', 'immigration', 'synfuels-corporation-cutback',
                    'education-spending', 'superfund-right-to-sue', 'crime',
                    'duty-free-exports', 'export-administration-act-south-africa']

voting_data = pd.read_csv('house-votes-84.data.txt', na_values=['?'],
                          names = feature_names)
# print(voting_data.head())

# voting_data.describe()

voting_data.dropna(inplace=True)
# voting_data.describe()

voting_data.replace(('y', 'n'), (1, 0), inplace=True)
voting_data.replace(('democrat', 'republican'), (1, 0), inplace=True)

# voting_data.head()

all_features = voting_data[feature_names].drop('party', axis=1).values
all_classes = voting_data['party'].values

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import cross_val_score

def create_model():
    model = Sequential()
    #first layer 16 inputs features
    model.add(Dense(32, input_dim=16, kernel_initializer='normal', activation='relu'))
    #hidden layers
    model.add(Dense(16, kernel_initializer='normal', activation='relu'))
    #output layers
    model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
    #compile model using binary beacuse the output can by 1 or 0 
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    return model

from keras.wrappers.scikit_learn import KerasClassifier
estimator = KerasClassifier(build_fn=create_model, nb_epoch=1000, verbose=0)

cv_scores = cross_val_score(estimator,all_features,all_classes,cv=10)
print(cv_scores.mean())
