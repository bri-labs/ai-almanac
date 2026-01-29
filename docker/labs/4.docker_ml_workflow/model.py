# Responsible for training the Machine Learning model
# Should not be concerned with APIs
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df=pd.read_csv("data/iris.csv")

# Drop species column
X=df.drop("Species", axis=1)
y=df['Species']

# split dataset
X_train, x_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf=RandomForestClassifier(n_estimators=50, random_state=42)
clf.fit(X_train, y_train)

# Save the model
joblib.dump(clf, "iris_model.pkl")
print("The model is trained and saved")