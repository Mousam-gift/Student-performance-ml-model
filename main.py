import pickle
import pandas as pd
 # load data sets
df = pd.read_csv("student_data_1000.csv")
#view first 5 row
print(df.head())
#data set info
print(df.info())

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df["coding_interest"] = encoder.fit_transform(df["coding_interest"])
df["final_performance"] = encoder.fit_transform(df["final_performance"])

print(df)



from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# Separate features (x) and target (y)
x = df.drop("final_performance", axis=1)
y = df["final_performance"]
# Split data into training & testing sets
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)
#Train Decision Tree model
dt = DecisionTreeClassifier(random_state=42)
dt.fit(x_train, y_train)
#Test Decision Tree accuracy
dt_pred = dt.predict(x_test)
dt_acc = accuracy_score(y_test, dt_pred)
#Train Random Forest model (IMPORTANT)
rf = RandomForestClassifier(n_estimators=100,random_state=42)
rf.fit(x_train, y_train)

with open("student_performance_model.pkl","wb")as file:
    pickle.dump(rf,file)
print("Model saved successfully!")


# Test Random Forest accuracy
rf_pred= rf.predict(x_test)
rf_acc= accuracy_score(y_test, rf_pred)
#Compare results
print("\nModel Accuracy Comparison")
print("Decision Tree Accuracy:", dt_acc)
print("Random Forest Accuracy:", rf_acc)

def recommend_career(attendance, math_score, science_score, coding_interest, performance):
    if performance == 1 and coding_interest == 1:
        return "Software Developer / Data Science"
    elif performance == 1 and science_score == 1:
        return "Engineering / Research"
    elif performance == 0:
        return "skill-based IT / Support roles"
    else:
        return "Foundation Courses / Diploma"
    

sample = x_test.iloc[0]
predicted_performance = rf.predict([sample])[0]

career = recommend_career(
    attendance=sample["attendance"],
    math_score=sample["math_score"],
    science_score=sample["science_score"],
    coding_interest=sample["coding_interest"],
    performance=predicted_performance
)

print("\nPredicted Performance Code:",predicted_performance)
print("Recommended Career Path:",career)

with open("student_performance_model.pkl","rb") as file:
    loaded_model = pickle.load(file)
loaded_prediction = loaded_model.predict(sample.to_frame().T)[0]    
print("Prediction from loaded model:",loaded_prediction)