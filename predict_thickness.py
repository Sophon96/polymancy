import pickle

# Load the trained model
with open("polyfilm_model.pkl", "rb") as f:
    model = pickle.load(f)

# Predict thickness
MW = 192000  # example molecular weight in Daltons
C = 20  # example concentration in mg/mL
predicted_thickness = model.predict_thickness(MW, C)
print(f"Predicted thickness: {predicted_thickness} nm")
