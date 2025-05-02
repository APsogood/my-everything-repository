import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Load the data from the local CSV file
data = pd.read_csv('./predict.csv')

# Ensure the data has at least 49 records
if len(data) < 49:
    raise ValueError("The dataset must contain at least 49 records.")

# Use the last 49 records
data = data.tail(49)

# Prepare the data
data['Index'] = np.arange(len(data))  # Create an index column for time
X = data[['Index']]  # Feature: time index
y = data['Close']    # Target: closing price

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the next stock price (index = 49)
next_index = [[len(data)]]
predicted_price = model.predict(next_index)

print(f"Predicted stock price for the next time step: {predicted_price[0]:.2f}")