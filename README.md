📄 Project Title: Fault Detection by Coordinates in 3D Model

1. Introduction
This project aims to automatically detect faults in 3D models by analyzing vibration sensor data and coordinate data extracted from .stl files. The main objective is to classify whether a fault is present at given coordinate points of a 3D object. This is achieved using multiple supervised machine learning models trained on vibration data collected through an ADXL345 sensor.

2. Dataset
The dataset used in this project is named ADXL345_SensorData.csv, containing four columns:
X-direction: X-axis vibration/coordinate value


Y-direction: Y-axis vibration/coordinate value


Z-direction: Z-axis vibration/coordinate value


Error_found: Indicates if an error (fault) was found at those coordinates (yes or no).


The target variable Error_found is encoded as 0 for no fault and 1 for fault detected.



3. Libraries and Technologies Used
Python Libraries:


pandas and numpy for data manipulation


matplotlib and seaborn for visualization


scikit-learn for model training and evaluation


xgboost for XGBoost classifier


imblearn for ADASYN oversampling


Flask for web deployment


numpy-stl (stl module) for reading .stl files


pickle for model saving and loading


Tools:


Jupyter Notebook / Python IDE for development


Flask framework for backend web application


HTML templates for frontend (upload form, result page)







4. Data Preprocessing
Key steps:
Checked for missing values and verified data integrity.


Visualized distributions using KDE plots and scatter plots to understand vibration patterns.


Detected and replaced outliers with median values using a custom percentile-based function.


Balanced the dataset using ADASYN to handle class imbalance.





5. Exploratory Data Analysis
Various plots were created:
KDE plots for X, Y, Z directions to check vibration distributions.


Scatter plot for X-direction vs Y-direction colored by Error_found.


Violin plot to visualize distribution differences by Error_found.


Heatmap to see correlations between vibration directions.


Boxplots to detect outliers before and after treatment.





6. Model Training and Selection
Multiple supervised models were tested:
Logistic Regression


Random Forest Classifier


XGBoost Classifier


Naive Bayes


K-Nearest Neighbors (KNN)


Support Vector Classifier (SVC)


Hyperparameter tuning was done using GridSearchCV for Random Forest, SVC, KNN, and XGBoost.


7. Model Evaluation
Models were evaluated using:


Classification Report (Precision, Recall)


Accuracy Score


F1 Score


ROC AUC Score


Comparative bar plots were created to compare F1 Scores and Accuracy Scores across models.


The best model (highest accuracy/F1) was selected and saved as model.pkl.
8. Backend Deployment
The Flask app handles:
A homepage and additional static pages.


A /predictor route for the prediction form.


A /predict route which:


Accepts .stl file uploads.


Reads the .stl file using numpy-stl.


Extracts all 3D coordinates.


Runs predictions using the saved model.


Displays the first 1000 predictions with x, y, z coordinates and whether a fault is detected.



9. STL File Handling
Uploaded .stl files are saved with a unique filename.


Coordinates are extracted using mesh.Mesh.from_file(filepath).


Coordinates are reshaped to feed directly into the trained model.


After prediction, the uploaded file is deleted automatically to keep the server clean.




10. Result
Predictions show each coordinate’s status:


"Fault Detected" if the model predicts a fault.


"No Fault" if no fault is detected.


Users can visually verify results on the web interface.



11. Future Improvements
Improve dataset size with more sensor readings.


Integrate visualization to highlight faulty coordinates on the 3D model.


Add user authentication for secure file uploads.


Deploy on a cloud platform for wider access.









✅ Conclusion
This project demonstrates a complete pipeline from sensor data collection to machine learning model deployment for automatic fault detection using vibration data and 3D coordinates. The solution provides an accessible web interface for users to upload .stl files and receive instant feedback on possible faults.

Attachments:
app.py: Flask application backend


test.py: Standalone prediction script


model.pkl: Trained model file


HTML templates: (not shared here)



Submitted By:
Siddharth Sharma(Team Leader)
Abeer Kumar(Member)
KeertanGupta(Member)
ANAND INTERNATIONAL COLLEGE OF ENGINEERING,JAIPUR

End of Document


