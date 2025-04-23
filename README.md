# 🩺 Revolutionizing Diabetes Management Using Machine Learning  
---

A smart **diet and exercise recommendation system** for diabetic individuals using Machine Learning techniques, built with a user-friendly interface to personalize health suggestions based on individual metrics like age, weight, glucose levels, and insulin usage.

---

## 📌 Project Overview

**Motivation:**  
With diabetes on the rise globally, maintaining optimal **diet and exercise routines** is critical. Traditional methods of diabetes management lack personalized insights. This project bridges that gap using data-driven models to provide users with **customized diet and workout suggestions**.

**Goal:**  
To improve diabetic patient care by automating:
- **Diet Recommendations**
- **Exercise Suggestions**

---

## 🎯 Objectives

- 📊 Predict appropriate **diet plans** based on:
  - Age, Weight, Height, Type of Diabetes, Glucose level, Insulin use
- 🏋 Recommend **exercise routines** tailored by:
  - Age and BMI

---

## 🔍 Dataset

- Format: CSV file (`diabetes_data.csv`)
- Features:
  - Age, Gender, Height, Weight, BMI, Glucose Level, Insulin Usage, Diabetes Type
- Labels:
  - `Diet_Recommendation` and `Exercise_Recommendation`

> Note: You can customize the file by adding fields such as `Meal Preferences`, `Activity Level`, or `Medical Restrictions`.

---

## ⚙️ Methodology

1. **Data Preprocessing**  
   - Handling missing values
   - Feature normalization (e.g., BMI calculation)
   - Label encoding

2. **Machine Learning Models Used**
   - Logistic Regression
   - Support Vector Machine (SVM)
   - K-Nearest Neighbors (KNN)
   - Random Forest 🌲
   - Naive Bayes
   - Gradient Boosting

3. **Model Evaluation**
   - Accuracy
   - Confusion Matrix
   - ROC-AUC Curve
   - Cross Validation (K=5)

---

## 🏆 Results

| Task                     | Accuracy   |
|--------------------------|------------|
| Diet Recommendation      | **93%**     |
| Exercise Recommendation  | **87.9%**   |

📈 Improvements possible with:
- More data
- Better clustering for similar patient profiles
- Incorporation of user feedback

---

## 💡 Future Enhancements

- 🏥 Integrate **doctor and clinic locator**
- 📅 Add **reminder system** for glucose checks
- 🧠 Use **deep learning models** for complex prediction
- 📲 Build mobile/web app with push notifications

---

## 🧪 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/diabetes-ml-recommendation.git
cd diabetes-ml-recommendation
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run app.py
```

## 📚 References

- Eva et al. (2022). Diabetes Health Care Routine Using ML. [DOI](https://doi.org/10.1109/ICEEICT53079.2022.9768659)  
- Singla et al. (2019). ML in Diabetes Care. [PMCID: PMC6844177](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6844177/)  
- Bhat & Ansari (2021). Diet Recommendation Using ML. [DOI](https://doi.org/10.1109/INCET51464.2021.9456365)

---
