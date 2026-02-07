import streamlit as st
import pandas as pd
import pickle

#load trained model
with open ("student_performance_model.pkl","rb")as file:
    model = pickle.load(file)

#career recomendation logic
def recommend_career(math_score, science_score, coding_interest,performance):
    if performance==1 and coding_interest==1:
        return "Software Developer / Data Science"
    elif performance==1 and science_score>=75:
        return "Engineering / Research"
    elif performance==0:
        return "Skill-based IT / Support roles"
    else:
        return "Foundation Courses / Diploma"
    
#streamlit ui
st.title("Student performance and career recommendation system")
st.write("Enter student details to predict performance path.")

attendance = st.slider("Attendence(%)",50,100,75)
math_score = st.slider("Math Score",35,100,70)
science_score = st.slider("Science Score",35,100,70)
coding_interest = st.selectbox("Coding Interest",["Yes","No"])

if coding_interest == "Yes":
    coding_interest_val = 1
else:
    coding_interest_val = 0

#predict button
if st.button("predict"):
    input_data = pd.DataFrame([[attendance, math_score, science_score, coding_interest_val]], columns=["attendance", "math_score", "science_score", "coding_interest"])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        performance = "Good"
    elif prediction == 0:
        performance = "Average"
    else:
        performance = "Poor"

    career = recommend_career(math_score, science_score, coding_interest_val, prediction)
    st.success(f"Predicted Performance:{performance}")
    st.info(f"Recommended Career Path: {career}")    