from flask import Flask, request, render_template, flash, redirect, url_for
import pickle
import numpy as np
from stl import mesh 
import os
import uuid  # Import the uuid module

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/portfolio-details")

def portfolio():
    return render_template("portfolio-details.html")

@app.route("/service")
def service():
    return render_template("service-details.html")

@app.route("/predictor")
def predictor():
    return render_template("starter-page.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Check if file was uploaded
        if 'stl_file' not in request.files:
            flash("No file selected")
            return redirect(request.url)
        
        stl_file = request.files['stl_file']
        
        # Verify file exists and has .stl extension
        if stl_file.filename == '':
            flash("No file selected")
            return redirect(request.url)
        
        if not stl_file.filename.lower().endswith('.stl'):
            flash("Please upload a valid .stl file")
            return redirect(request.url)
        
        try:
            # Create uploads directory if it doesn't exist
            upload_dir = "uploads"
            os.makedirs(upload_dir, exist_ok=True)
            
            # Save uploaded file with unique name
            filename = f"{uuid.uuid4()}.stl"  # Generate a unique filename
            filepath = os.path.join(upload_dir, filename)
            stl_file.save(filepath)
            
            # Process the STL file
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
            
            # Clean up by removing uploaded file
            os.remove(filepath)
            
            # Render results
            return render_template("results.html", predictions=results)
        
        except Exception as e:
            flash(f"Error processing file: {str(e)}")
            return redirect(request.url)
    
    return render_template("upload.html")  # Ensure this points to your upload page

if __name__ == "__main__":
    app.run(debug=True)
