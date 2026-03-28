import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 Ecovision Skill Recommender Tool")

# Inputs
edu = st.selectbox("Education", ["BA","BSc","BCom","BBA"])
coding = st.selectbox("Coding", ["No","Maybe","Yes"])
math = st.selectbox("Math Level", ["Low","Medium","High"])
interest = st.selectbox("Interest", ["Data","Business","Research","Tech"])

# Mapping
edu_map = {"BA":1,"BSc":2,"BCom":3,"BBA":4}
coding_map = {"No":0,"Maybe":1,"Yes":2}
math_map = {"Low":0,"Medium":1,"High":2}
interest_map = {"Data":1,"Business":2,"Research":3,"Tech":4}

# Prediction
if st.button("Get Recommendation"):
    input_data = [[
        edu_map[edu],
        interest_map[interest],
        1,
        coding_map[coding],
        math_map[math],
        1,
        1,
        1
    ]]
    
    result = model.predict(input_data)[0]
    st.success(f"Recommended: {result}")