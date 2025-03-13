from sklearn.tree import DecisionTreeClassifier

# Sample data: age and income used to classify purchasing behavior (1 = buys, 0 = doesn't buy)
X = [[25, 50000], [35, 60000], [45, 70000], [20, 40000], [30, 50000]]
y = [1, 1, 0, 0, 1]  # purchasing behavior

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Prediction
prediction = model.predict([[40, 65000]])  # Predict purchasing behavior
print(f"Predicted purchasing behavior for age 40 with income 65000: {prediction[0]}")
