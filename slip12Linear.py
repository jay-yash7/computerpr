from sklearn.linear_model import LinearRegression

# Sample dataset (X: input, y: output)
X = [[1], [2], [3], [4], [5]]  # Features
y = [2, 4, 6, 8, 10]  # Target (y = 2x)

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Predict for a new value
new_x = [[6]]
predicted_y = model.predict(new_x)

print("Predicted value for 6:", predicted_y[0])
