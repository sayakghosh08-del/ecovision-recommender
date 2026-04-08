import streamlit as st
import pickle
import pandas as pd
import os

# Logo
st.image("logo.png", width=150)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.markdown("# 🎓 Ecovision Academy")
st.markdown("## 🚀 Skill Recommender Tool")
st.markdown("---")

# Student info
name = st.text_input("👤 Student Name")
phone = st.text_input("📞 Phone Number")

# Inputs
edu = st.selectbox("🎓 Education", ["BA/MA", "BSc/MSc", "BCom/MCom", "BBA/MBA"])
interest = st.selectbox("💡 Interest", ["Tech", "Business", "Research", "Creative"])
vibe = st.selectbox("✨ Work Style", ["Analytical", "Practical", "Creative"])
coding = st.selectbox("💻 Coding Interest", ["Yes", "No"])
math = st.selectbox("📊 Math Comfort", ["High", "Medium", "Low"])
work = st.selectbox("🏢 Work Preference", ["Corporate", "Freelance", "Academic"])
speed = st.selectbox("⚡ Learning Speed", ["Fast", "Medium", "Slow"])
scenario = st.selectbox("🧩 Scenario", ["Data", "Finance", "Charts", "AI"])

# Mapping (IMPORTANT)
edu_map = {"BA/MA":0, "BSc/MSc":1, "BCom/MCom":2, "BBA/MBA":3}
interest_map = {"Tech":0, "Business":1, "Research":2, "Creative":3}
vibe_map = {"Analytical":0, "Practical":1, "Creative":2}
coding_map = {"Yes":1, "No":0}
math_map = {"High":2, "Medium":1, "Low":0}
work_map = {"Corporate":0, "Freelance":1, "Academic":2}
speed_map = {"Fast":2, "Medium":1, "Slow":0}
scenario_map = {"Data":0, "Finance":1, "Charts":2, "AI":3}

# Button
if st.button("Get Recommendation"):

    if name == "" or phone == "":
        st.warning("⚠️ Please enter your name and phone number")

    else:
        # Save data
        data = {"Name": name, "Phone": phone}

        if os.path.exists("students.csv"):
            df = pd.read_csv("students.csv")
            df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        else:
            df = pd.DataFrame([data])

        df.to_csv("students.csv", index=False)

        # Prepare input
        input_data = [[
            edu_map[edu],
            interest_map[interest],
            vibe_map[vibe],
            coding_map[coding],
            math_map[math],
            work_map[work],
            speed_map[speed],
            scenario_map[scenario]
        ]]

        # Prediction
        result = model.predict(input_data)[0]

        # Output
        st.success(f"🎯 {name}, Recommended: {result}")

        if result == "Excel":
            st.write("👉 Start with Excel → Power BI → SQL")

        elif result == "Python":
            st.write("👉 Start with Python → Machine Learning → AI")

        elif result == "PowerBI":
            st.write("👉 Start with Excel → Power BI → Dashboarding")

        elif result == "Stata":
            st.write("👉 Start with Stata → Econometrics → Research")

# Download button
if os.path.exists("students.csv"):
    df = pd.read_csv("students.csv")

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="📥 Download Student Data",
        data=csv,
        file_name='students.csv',
        mime='text/csv'
    )
