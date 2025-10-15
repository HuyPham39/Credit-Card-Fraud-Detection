import pandas as pd


from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import precision_score, recall_score, fbeta_score, average_precision_score, confusion_matrix


# Load the data in
df = pd.read_csv("ETLdata.csv")
X = df.drop(['Class'], axis=1)
Y = df.Class

# Split data into training/testing folds

kfold = KFold(n_splits=10, 
              shuffle=True, 
              random_state=0)


