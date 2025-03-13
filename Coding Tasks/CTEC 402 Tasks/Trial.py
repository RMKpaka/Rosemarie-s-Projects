import pandas as pd

# Load dataset
file_path = r"C:\Users\Rosemarie\Documents\Rosemarie\CTEC 402 Class Fall 2024\synthetic_network_traffic.csv"
data = pd.read_csv(file_path)  # Read CSV file into DataFrame

# Data preprocessing
if 'IsAnomaly' not in data.columns:
    raise KeyError("'IsAnomaly' column not found in the dataset.")

X = data.drop(columns=['IsAnomaly'])  # Features
y = data['IsAnomaly']  # Target variable

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Build the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.callbacks import EarlyStopping

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
history = model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test),
                    callbacks=[EarlyStopping(monitor='val_loss', patience=5)], verbose=1)
