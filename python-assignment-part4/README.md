# 📊 Part 4 — Data Visualization & Machine Learning

## 🎯 Objective
The goal of this assignment was to analyse student performance data, create meaningful visualizations, and build a simple machine learning model to predict whether a student will pass or fail.

---

## 📁 Dataset
The dataset used is `students.csv`.

It contains:
- Subject marks: Math, Science, English, History, PE
- Attendance percentage
- Study hours per day
- Final result (`passed`: 1 = Pass, 0 = Fail)

---

## 🔍 Task 1 — Data Exploration
- Loaded the dataset using pandas
- Displayed first few rows using `.head()`
- Checked dataset shape and data types
- Used `.describe()` to view summary statistics
- Counted number of students who passed and failed
- Calculated average subject scores for pass and fail groups
- Identified the student with the highest overall average

---

## 📈 Task 2 — Data Visualization (Matplotlib)
Created and saved the following plots:

1. Bar chart — Average score per subject  
2. Histogram — Distribution of math scores  
3. Scatter plot — Study hours vs average score  
4. Box plot — Attendance comparison (Pass vs Fail)  
5. Line plot — Math vs Science scores  

All plots are saved as `.png` files.

---

## 🎨 Task 3 — Data Visualization (Seaborn)
- Created bar plots comparing math and science scores based on pass/fail
- Created scatter plot with regression lines for attendance vs average score

**Observation:**  
Seaborn was easier for statistical plots and required less code, while Matplotlib gave more flexibility but needed more manual setup.

---

## 🤖 Task 4 — Machine Learning
Used Logistic Regression to predict whether a student will pass or fail.

### Steps:
- Selected features:
  - Subject marks
  - Attendance
  - Study hours
- Split data into training and testing sets (80/20)
- Scaled data using StandardScaler
- Trained the model
- Evaluated using training and test accuracy
- Compared predicted vs actual results
- Extracted feature importance (model coefficients)
- Plotted feature importance

---

## 🔮 Bonus — Prediction
Tested the model on a new student’s data and predicted:
- Pass/Fail result
- Probability of prediction

---

## 🛠️ Libraries Used
- pandas  
- matplotlib  
- seaborn  
- scikit-learn  

---

## 📂 Files Included
- `part4_visualization_ml.ipynb`
- `students.csv`
- Plot images:
  - `plot1_bar.png`
  - `plot2_hist.png`
  - `plot3_scatter.png`
  - `plot4_box.png`
  - `plot5_line.png`
  - `plot6_seaborn_bar.png`
  - `plot7_seaborn_scatter.png`
  - `plot8_feature_importance.png`

---

## 📌 Notes
- The dataset is small, so model accuracy may not be perfect.
- The focus was on understanding the complete workflow:
  data → visualization → model → prediction.

---

## ✅ Status
All tasks completed successfully with working outputs and saved plots.
