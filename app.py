import streamlit as st
import pickle
import pandas as pd
import os
st.image("logo.png", width=150)

model = pickle.load(open("model.pkl", "rb"))

st.markdown("# 🎓 Ecovision Academy")
st.markdown("## 🚀 Skill Recommender Tool")
st.markdown("---")

# Student info
name = st.text_input("👤 Student Name")
phone = st.text_input("📞 Phone Number")

# Inputs
edu = st.selectbox("🎓 Education", ["BA/MA","BSc/MSc","BCom/MCom","BBA/MBA"])

interest = st.selectbox("🎯 What excites you?",
["Working with data","Business insights","Research","Tech"])

vibe = st.selectbox("💼 Career vibe",
["Corporate","Research","Tech","Government"])

coding = st.selectbox("💻 Coding?", ["No","Maybe","Yes"])

math = st.selectbox("🧠 Math level", ["Low","Medium","High"])

work = st.selectbox("🧩 Work style",
["Charts","Code","Theory","Business problems"])

speed = st.selectbox("⏳ Learning speed",
["Fast job","Medium","Deep learning"])

scenario = st.selectbox("🧪 Pick a scenario",
["Charts","Code","Research","Business"])

# Mapping
edu_map = {"BA/MA":1,"BSc/MSc":2,"BCom/MCom":3,"BBA/MBA":4}
interest_map = {"Working with data":1,"Business insights":2,"Research":3,"Tech":4}
vibe_map = {"Corporate":1,"Research":2,"Tech":3,"Government":4}
coding_map = {"No":0,"Maybe":1,"Yes":2}
math_map = {"Low":0,"Medium":1,"High":2}
work_map = {"Charts":1,"Code":2,"Theory":3,"Business problems":4}
speed_map = {"Fast job":0,"Medium":1,"Deep learning":2}
scenario_map = {"Charts":1,"Code":2,"Research":3,"Business":4}

# Prediction
if st.button("Get Recommendation"):
    
   if name == "" or phone == "":
    st.warning("⚠️ Please enter your name and phone number")

else:
    data = {"Name": name, "Phone": phone}

    if os.path.exists("students.csv"):
        df = pd.read_csv("students.csv")
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    else:
        df = pd.DataFrame([data])

    df.to_csv("students.csv", index=False)

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

    result = model.predict(input_data)[0]

st.success(f"🎯 {name}, Recommended: {result}")

if result == "Excel":
    st.write("👉 Start with Excel → Power BI → SQL")

elif result == "Python":
    st.write("👉 Start with Python → Machine Learning → AI")

elif result == "PowerBI":
    st.write("👉 Start with Excel → Power BI → Dashboarding")

elif result == "Stata":
    st.write("👉 Start with Stata → Econometrics → Research")
