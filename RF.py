import numpy as np
from sklearn.ensemble import RandomForestClassifier 
import pandas
from sklearn.externals import joblib

#define the model
rf = RandomForestClassifier(n_estimators=50, oob_score=True)
#train the model
rf = rf.fit(img09, data09)

#save model
filename = "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf.sav"
joblib.dump(rf, filename)

#predict 2009
result09 = rf.predict(img09)

#save result into Numpy Array file
a = "/Volumes/ga87rif/Study Project/satelite images/result09.npy"
np.save(a, result09)

#predict 2015
result15 = rf.predict(img15)

#save result into Numpy Array file
a = "/Volumes/ga87rif/Study Project/satelite images/result15.npy"
np.save(a, result15)

#predict 2018
result18 = rf.predict(img15)

#save result into Numpy Array file
a = "/Volumes/ga87rif/Study Project/satelite images/result18.npy"
np.save(a, result18)