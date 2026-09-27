import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

normal_data = np.array([
    [10, 30, 40],
    [15, 35, 42],
    [20, 40, 45],
    [18, 38, 44],
    [25, 42, 48],
    [12, 32, 41],
    [22, 39, 46],
    [17, 36, 43],
    [20, 41, 47],
    [14, 34, 40]
])

model = IsolationForest(
    contamination=0.1,
    random_state=42
)

model.fit(normal_data)

joblib.dump(model, "ai/model.pkl")

print("AI anomaly detection model trained successfully.")
print("Model saved as ai/model.pkl")