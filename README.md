# 🎓 Student Performance Predictor

A machine learning project that predicts student academic performance and recommends career paths using Decision Tree and Random Forest classifiers.


---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Career Recommendation Logic](#career-recommendation-logic)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## 🧠 Overview

This project uses supervised machine learning to analyze student data and predict their final academic performance. Based on the prediction, it also recommends suitable career paths — helping educators and students make data-driven decisions.

The pipeline includes:
- Data preprocessing with Label Encoding
- Training two classifiers: Decision Tree and Random Forest
- Model comparison by accuracy
- Saving/loading the best model using `pickle`
- Career path recommendation based on predicted performance

---

## ✨ Features

- ✅ Predicts student final performance (e.g., Pass / Fail / Average)
- ✅ Compares Decision Tree vs Random Forest accuracy
- ✅ Saves the trained Random Forest model for reuse
- ✅ Recommends career paths based on prediction + student profile
- ✅ Model persistence with `pickle`

---

## 📁 Project Structure

```
student-performance-predictor/
│
├── student_data_1000.csv              # Dataset (1000 student records)
├── student_performance_model.pkl      # Saved Random Forest model
├── student_performance_predictor.py   # Main script
└── README.md                          # Project documentation
```

---

## 📊 Dataset

The dataset `student_data_1000.csv` contains **1000 student records** with the following features:

| Column | Description | Type |
|---|---|---|
| `attendance` | Attendance percentage | Numeric |
| `math_score` | Score in Mathematics | Numeric |
| `science_score` | Score in Science | Numeric |
| `coding_interest` | Interest in coding (Yes/No) | Categorical |
| `final_performance` | Target variable (performance label) | Categorical |

> ⚠️ The `coding_interest` and `final_performance` columns are label-encoded before training.

---

## ⚙️ Installation

### Prerequisites

Make sure you have **Python 3.7+** installed.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-performance-predictor.git
cd student-performance-predictor
```

### 2. Install dependencies

```bash
pip install pandas scikit-learn
```

Or use a `requirements.txt`:

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
pandas
scikit-learn
```

---

## 🚀 Usage

### Run the predictor

```bash
python student_performance_predictor.py
```

### What happens when you run it:

1. Loads and preprocesses the dataset
2. Encodes categorical columns
3. Splits data into training (80%) and testing (20%) sets
4. Trains a **Decision Tree** and a **Random Forest** model
5. Saves the Random Forest model to `student_performance_model.pkl`
6. Prints accuracy comparison
7. Predicts performance for a sample student
8. Recommends a career path
9. Reloads the saved model and verifies the prediction

### Sample Output

```
Model Accuracy Comparison
Decision Tree Accuracy: 0.87
Random Forest Accuracy: 0.93

Predicted Performance Code: 1
Recommended Career Path: Software Developer / Data Science

Prediction from loaded model: 1
```

---

## 🤖 Model Details

### Decision Tree Classifier

- **Algorithm:** CART (Classification and Regression Trees)
- **random_state:** 42
- Simple and interpretable, but prone to overfitting

### Random Forest Classifier ⭐ (Saved Model)

- **Algorithm:** Ensemble of 100 Decision Trees
- **n_estimators:** 100
- **random_state:** 42
- More robust, higher accuracy, less prone to overfitting
- This is the model saved to `student_performance_model.pkl`

### Train/Test Split

| Set | Size |
|---|---|
| Training | 80% (800 samples) |
| Testing | 20% (200 samples) |

---

## 🗺️ Career Recommendation Logic

Based on the predicted performance and student attributes, the system recommends:

| Condition | Recommended Career |
|---|---|
| High performance + Coding interest | Software Developer / Data Science |
| High performance + Strong science score | Engineering / Research |
| Low performance | Skill-based IT / Support Roles |
| Otherwise | Foundation Courses / Diploma |

---

## 📈 Results

| Model     | Accuracy |
|---------------|------|
| Decision Tree | ~87% |
| Random Forest | ~93% |

> Note: Actual accuracy may vary slightly depending on the dataset.

---

## 🔮 Future Improvements

- [ ] Add cross-validation for more reliable accuracy estimates
- [ ] Hyperparameter tuning with `GridSearchCV`
- [ ] Replace `pickle` with `joblib` for safer model serialization
- [ ] Build a simple web UI with Flask or Streamlit
- [ ] Add more features (e.g., extracurricular activities, socioeconomic background)
- [ ] Use SMOTE for handling class imbalance
- [ ] Add data visualization (feature importance, confusion matrix)

---

## 🛡️ Notes

- This project uses `pickle` for model serialization. For production use, consider switching to `joblib` which is safer and more efficient for large NumPy arrays.
- Ensure the CSV column order matches the feature order used during training when making new predictions.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Your Name**  
GitHub: [Mousam-gift](https://github.com/Mousam-gift)  
Feel free to open issues or submit pull requests!

---

⭐ If you found this project helpful, please give it a star!
