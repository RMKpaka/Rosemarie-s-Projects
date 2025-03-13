from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data: hours studied vs. exam score
X = np.array([[1], [2], [3], [4], [5]])  # hours studied
y = np.array([2, 4, 5, 4, 5])  # exam score

# Train the model
model = LinearRegression()
model.fit(X, y)

# Prediction
score_prediction = model.predict([[6]])  # Predict score for 6 hours studied
print(f"Predicted exam score for 6 hours of study: {score_prediction[0]:.2f}")
