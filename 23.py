from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load the dataset into a pandas dataframe
df = pd.read_csv('dataset.csv')

# Preprocess the categorical variables like 'device_type' using LabelEncoder
le = LabelEncoder()
df['device_type'] = le.fit_transform(df['device_type'])

# Split the dataset into training and testing sets
X = df.drop('purchase', axis=1)
y = df['purchase']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier and fit it to the training data
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict whether a new customer will make a purchase or not
new_customer = [[25, 50000, 10, 'mobile']]
new_customer[0][3] = le.transform([new_customer[0][3]])[0]
prediction = clf.predict(new_customer)
print(prediction)
