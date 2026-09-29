import joblib
import pandas as pd

model = joblib.load("house_price_model.pkl")

sample = pd.DataFrame([{
    "MedInc": 5.0, "HouseAge": 20.0, "AveRooms": 5.0,
    "AveBedrms": 1.0, "Population": 1000.0, "AveOccup": 3.0,
    "Latitude": 34.0, "Longitude": -118.0
}])

prediction = model.predict(sample)[0]
print(f"Predicted house value: ${prediction * 100000:,.0f}")
