import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

data = {
    'weight': [150, 130, 120, 160, 140, 130],
    'color': ['red', 'green', 'yellow', 'red', 'green', 'yellow'],
    'texture': ['smooth', 'rough', 'smooth', 'rough', 'smooth', 'rough'],
    'type': ['apple', 'orange', 'banana', 'apple', 'orange', 'banana']
}

df = pd.DataFrame(data)

X = df[['weight', 'color', 'texture']]
y = df['type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['weight']),
        ('cat', OneHotEncoder(), ['color', 'texture'])
    ])


knn_classifier = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', KNeighborsClassifier(n_neighbors=3))  
])


knn_classifier.fit(X_train, y_train)
y_pred = knn_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
