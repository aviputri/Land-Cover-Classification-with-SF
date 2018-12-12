import numpy as np 
from sklearn.metrics import accuracy_score, confusion_matrix

#accuracy_score(y_true, y_pred)
accuracy_score(data09, result09)
#calculate 
#confusion_matrix(y_true, y_pred, labels=None, sample_weight=None)
confusion_matrix(data09, result09, labels=[1,2,3,4,5,6,7,8])