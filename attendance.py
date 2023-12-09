import streamlit as st
import cv2
import numpy as np
import pandas as pd
import face_recognition
import os
from datetime import date

def takeAttendance():
    studentFaces = []
    studentNames = []
    folder = "./Students/"
    for file in os.listdir(folder):
        studentImage = face_recognition.load_image_file((os.path.join(folder, file)))
        studentEncoding = face_recognition.face_encodings(studentImage)[0]
        studentFaces.append(studentEncoding)
        studentNames.append(file.split("_")[0])

    image = st.camera_input("Capture Image")

    if image is not None:
        bytesData = image.getvalue()
        imageArray = cv2.imdecode(np.frombuffer(bytesData, np.uint8), cv2.IMREAD_COLOR)

        filename = "./Attendance/" + str(date.today()) + ".jpg"
        with open(filename, 'wb') as file:
            file.write(image.getbuffer())

        faceLocations = face_recognition.face_locations(imageArray)

        regionOfInterest = [imageArray[top:bottom+5, left:right+5].copy() for (top, right, bottom, left) in faceLocations]

        st.write("Number of faces in picture :", len(faceLocations))

        if faceLocations:
            dataFrames = []

            for faceIndex, roi in enumerate(regionOfInterest):
                face = face_recognition.face_encodings(roi)
                matches = face_recognition.compare_faces(studentFaces, face[0])
                matchedNames = [studentNames[i] for i, match in enumerate(matches) if match]

                status = ["Present" if studentName in matchedNames else "Absent" for studentName in studentNames]

                dataFrames.append(pd.DataFrame({
                    "Student Name" : studentNames,
                    "Status" : status
                }))
            result = pd.concat(dataFrames).sort_values(by="Student Name", ascending=True)
            return result

def viewAttendance(attendanceDf):
    st.write(attendanceDf)