# Fault Detection by Coordinates in 3D Model

## 📌 Project Overview
This project detects **faults in 3D models** by analyzing vibration sensor data and 3D coordinate data extracted from `.stl` files.  
Using supervised machine learning models trained on vibration readings from an **ADXL345 sensor**, the system classifies whether a given coordinate point contains a fault.

The project also includes a **Flask-based web application** where users can upload `.stl` files and receive predictions for each coordinate.

---

## 📂 Dataset
**File:** `ADXL345_SensorData.csv`  

**Columns:**
- **X-direction** → X-axis vibration/coordinate value  
- **Y-direction** → Y-axis vibration/coordinate value  
- **Z-direction** → Z-axis vibration/coordinate value  
- **Error_found** → Fault presence (`1` = Fault, `0` = No Fault)  

---

## 🛠 Libraries & Technologies
- **Python** (pandas, numpy, scikit-learn, matplotlib, seaborn, xgboost, imblearn)
- **Flask** for backend deployment
- **numpy-stl** for `.stl` file processing
- **pickle** for model saving/loading
- **HTML/CSS** for frontend templates

---

## 🔍 Data Preprocessing
- Checked for missing values
- Visualized data distributions (KDE plots, scatter plots, violin plots, heatmaps)
- Removed/replaced outliers using a percentile-based median replacement
- Balanced dataset using **ADASYN** (to handle class imbalance)

---

## 📊 Exploratory Data Analysis (EDA)
- KDE plots for X, Y, Z directions
- Scatter plot of X vs Y with fault coloring
- Violin plots for vibration vs fault status
- Heatmap for correlation
- Boxplots before/after outlier removal

---

## 🤖 Model Training
Tested multiple ML models:
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- Naive Bayes
- K-Nearest Neighbors (KNN)
- Support Vector Classifier (SVC)

Performed **GridSearchCV** hyperparameter tuning for Random Forest, SVC, KNN, and XGBoost.  
Best-performing model was saved as **`model.pkl`**.

---

## 📈 Model Evaluation
Evaluated using:
- Accuracy Score
- F1 Score
- Precision & Recall
- ROC AUC Score

Created comparative bar plots for Accuracy and F1 scores.

---

## 🌐 Web Deployment
Flask Application Features:
- Homepage for file upload
- `/predict` route:
  - Accepts `.stl` files
  - Extracts 3D coordinates using `numpy-stl`
  - Predicts fault/no fault using trained model
  - Displays first 1000 predictions

Uploaded `.stl` files are deleted after processing to save space.

---

📁 project/
├── app.py # Flask backend                                                                                                   
├── test.py # Standalone prediction script                                                                                   
├── model.pkl # Trained ML model                                                                                             
├── ADXL345_SensorData.csv # Dataset                                                                                         
├── templates/ # HTML frontend files                                                                                         
├── static/ # CSS/JS files                                                                                                   
├── requirements.txt # Required Python packages                                                                              
└── README.md # Documentation                                                                                                                                                                                                                                                  

---

## 🚀 Installation & Usage
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/3D-Fault-Detection.git
cd 3D-Fault-Detection

pip install -r requirements.txt
python app.py



```


demo video link:-  https://drive.google.com/drive/folders/14-1T5GuMW8ydx0D-1ZsOEeLDIk3y02vV

