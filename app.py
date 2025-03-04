#streamlite
import streamlit as st

st.set_page_config(page_title="growth mindset project")
st.title("Growth Mindset Challenge: Web App with Streamlit")
st.header("Welcome to the Growth Mindset Challenge!")
st.write("Embrace the challenge and learn something new today!")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill")

st.header("What's your challenge today?")
user_input = st.text_input("Describe you are facing:")

#condition

if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward towards your goals!")
else:
    st.warning("Tell us about your challenge today!")

#reflecting
st.header("Reflect on your challenge")
user_reflection = st.text_area("Write your reflection here:")
if user_reflection:
    st.success(f"Great insight! Your reflection: {user_reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")

#achievement
st.header("Celebrate your wins!")
user_achievement = st.text_input("Share something you have accomplished:")

if user_achievement:
    st.success(f"Amazing! You have achieved: {user_achievement}")
else:
    st.info("Big or small, every achievement counts.")

#footer
st.write("- - -")
st.write("Keep believing in yourself. Growth is a journey, not a destination.")
st.write("⭐️ Created by [![GitHub](https://img.shields.io/badge/GitHub-KhuldoonAhmed-blue?logo=github)](https://github.com/Khuldoon171/Khuldoongrowth)")