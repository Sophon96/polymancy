import pickle
from polymancy import PolyFilmModel, load_data, preprocess_data

# Load and preprocess data
data = load_data("data/192k.csv")
X, y = preprocess_data(data)

# Train the model
model = PolyFilmModel()
model.train(X, y)

# Evaluate the model
mean_mse, std_mse = model.evaluate(X, y)
print(f"Mean Cross-Validation MSE: {mean_mse}")
print(f"Standard Deviation of MSE: {std_mse}")

# Save the trained model parameters
with open("polyfilm_model.pkl", "wb") as f:
    pickle.dump(model, f)
