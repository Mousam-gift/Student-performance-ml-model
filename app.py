import streamlit as st
import pandas as pd
import pickle

#load trained model
with open ("student_performance_model.pkl","rb")as file:
    data = pickle.load(file)
    model = data["model"]
    coding_encoder = data["coding_encoder"]
    performance_encoder = data["performance_encoder"]

#career recomendation logic
def recommend_career(math_score, science_score, coding_interest,performance):
    if performance=="Good" and coding_interest==1:
        return "Software Developer / Data Science"
    elif performance=="Good" and science_score>=75:
        return "Engineering / Research"
    elif performance=="Average":
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


#predict button
if st.button("predict"):
    coding_interest_val = coding_encoder.transform([coding_interest])[0]
    input_data = pd.DataFrame([[attendance, math_score, science_score, coding_interest_val]], columns=["attendance", "math_score", "science_score", "coding_interest"])
    prediction = model.predict(input_data)[0]

    performance = performance_encoder.inverse_transform([prediction])[0]

    career = recommend_career(math_score, science_score, coding_interest_val, performance)
    st.success(f"Predicted Performance:{performance}")
    st.info(f"Recommended Career Path: {career}")    
