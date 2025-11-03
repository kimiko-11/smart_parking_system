

# 🚗 Smart Parking Availability Prediction

This project predicts whether a parking slot will be **Occupied (1)** or **Vacant (0)** using machine learning, based on sensor and environmental data.

---

### ✅ Project Summary

We use a dataset containing parking information such as:

| Feature           | Meaning                             |
| ----------------- | ----------------------------------- |
| Timestamp         | Date & time of parking event        |
| Parking_Spot_ID   | Unique ID of each parking spot      |
| Sensor readings   | Proximity, pressure, ultrasonic     |
| Vehicle details   | Weight, height, etc.                |
| Weather & Traffic | Temp, precipitation, nearby traffic |
| Occupancy Status  | Target → 1 (occupied) / 0 (vacant)  |

The goal is to train a model that **predicts parking availability ahead of time**.

---

### 🔄 What Our Code Does (Step-by-Step)

1️⃣ **Load Data**
Read the CSV file and inspect data structure.

2️⃣ **Feature Engineering**

* Convert timestamp to:

  * hour of day
  * day of week
  * weekend or weekday
* Create `prev_occupancy` feature using history per parking slot
  → Helps the model learn patterns over time

3️⃣ **Encoding**
Convert text columns (like User Type, Vehicle Type) into numeric values using One-Hot Encoding.

4️⃣ **Train-Test Split**
Separate data into:

* Training set (for learning)
* Testing set (for evaluation)

5️⃣ **Model Training**
Train a **Random Forest Classifier** to predict occupancy.

6️⃣ **Model Evaluation**
Check accuracy score to see how well the model performs.

7️⃣ **Save the Model**
Export as `parking_model.pkl` so it can be used in a real app.

---

### 🛠 Tools & Libraries

* Python
* Pandas, NumPy
* Scikit-learn (Machine Learning)
* Imbalanced-learn (Handling class imbalance)
* Joblib (Model saving)

---

### 🚀 Future Scope

* Live camera + sensors
* Deployment as a mobile / web app
* Show available parking spots on a map
* Predict future availability based on patterns


Would you like me to create those too?
