import streamlit as st
from streamlit_option_menu import option_menu
from attendance import takeAttendance, viewAttendance
from students import addNewStudent
import pandas as pd

st.sidebar.image("https://media.licdn.com/dms/image/D4D03AQEIDlgfGR9CnA/profile-displayphoto-shrink_800_800/0/1679106793787?e=1707350400&v=beta&t=d84AUYEDkfx183T__KUTgFTEkfP52TpwoA09_51H3tg")
st.sidebar.markdown('''
            > Made by [*Bhavesh Mittal*](https://www.linkedin.com/in/bhavesh-mittal-602a36254)
''')

menuOptions = option_menu(None, ["Take Attendance", "View Attendance", "Add new student"], icons=["camera", "clock-history", "person-plus"], orientation="horizontal")

if 'attendanceDf' not in st.session_state:
    st.session_state.attendanceDf = pd.DataFrame(columns=["Student Name", "Status"])

if menuOptions == "Take Attendance":
    st.session_state.attendanceDf = takeAttendance()

elif menuOptions == "View Attendance":
    viewAttendance(st.session_state.attendanceDf)

elif menuOptions == "Add new student":
    addNewStudent()