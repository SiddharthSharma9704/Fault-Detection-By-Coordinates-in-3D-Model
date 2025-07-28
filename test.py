import pickle
import numpy as np
from stl import mesh

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

def run_prediction(filepath):
    your_mesh = mesh.Mesh.from_file(filepath)
    all_coordinates = your_mesh.vectors.reshape(-1, 3)
    results = []
    
    # Predict for all coordinates at once
    predictions = model.predict(all_coordinates)
    
    for i, (coords, pred) in enumerate(zip(all_coordinates[:1000], predictions[:1000])):  # Adjustable limit
        results.append({
            "index": i + 1,
            "x": round(coords[0], 2),
            "y": round(coords[1], 2),
            "z": round(coords[2], 2),
            "result": "Fault Detected" if pred else "No Fault"
        })
    
    return results
 