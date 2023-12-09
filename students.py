import streamlit as st
import uuid

def addNewStudent():
    col1, col2, col3 = st.columns(3)
    faceName = col1.text_input("Enter name")

    pic = col2.radio("Picture", options=["Upload from device", "Take a picture"])
    if pic == "Upload from device":
        image = col3.file_uploader("Upload Picture", type=[".jpg", ".png", ".jpeg"])
    else:
        image = col3.camera_input("Capture Image")

    if faceName and image:
        filename = "./Students/" + faceName + "_" + str(uuid.uuid1()) + ".jpg"
        with open(filename, 'wb') as file:
            file.write(image.getbuffer())