#streamlite
import streamlite as st # type: ignore


st.set_page_config(page_title="growth mindset project", project_icon="⭐")
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
    st.sucess(f"you re facing:{user_input}.keep pushing forward towards your goals!")
else:
    st.warning("tell us about your challenge today!")

    #reflexing
    st.header("Reflect on your challenge")
    user_reflection = st.text_area("Write your reflection here:")
    if user_reflection:
        st.sucess(f"Great insight!your reflection:{user_reflection}")
    else:
        st.info("Reflecting on past experience help you grow! Share your difficulties")

        #achievment
        st.header("Clerebrate your wins!")
        user_achievment = st.text_input("Share something you are accomplished:")

        if user_achievment:
            st.sucess(f"Awazing you are achieved:{user_achievment}")
        else:
            st.info("Big or small, every achievment counts")

            #footer
            st.write("- - -")
            st.write("Keep believing in youself. Growth is a journey, not a destination.")
            st.write("⭐️ Created by [Khuldoon Ahmed]")