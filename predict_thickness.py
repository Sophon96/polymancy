from polymancy import PolyFilmModel, load_data, preprocess_data

# Load and preprocess data
data = load_data("data/192k.csv")
X, y = preprocess_data(data)

# Train the model
model = PolyFilmModel(degree=2)
model.train(X, y)

# Predict thickness
MW = 192000  # example molecular weight in Daltons
C = 20  # example concentration in mg/mL
predicted_thickness = model.predict_thickness(MW, C)
print(f"Predicted thickness: {predicted_thickness} Å")
