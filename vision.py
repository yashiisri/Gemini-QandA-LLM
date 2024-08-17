from dotenv import load_dotenv

load_dotenv()  ## loading all the envirenoment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load gemini pro model and get responses
model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input!="":
         response=model.generate_content([input,image])
    else:
         response=model.generate_content(image)
    return response.text



##initialize our streamlit app

st.set_page_config(
    page_title="Gemini Image Demo",  # Title of the web page
    page_icon=":camera:",            # Icon that appears in the browser tab (you can use an emoji or path to an icon)
    layout="centered",               # Layout of the app ("centered" or "wide")
    initial_sidebar_state="auto"     # Sidebar state ("auto", "expanded", "collapsed")
)

st.header("Gemini Application")
input=st.text_input("Input Prompt:",key="input")

uploaded_file=st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
     image=Image.open(uploaded_file)
     st.image(image,caption="Uploaded Image",use_column_width=True)


submit=st.button("Tell me about the image")

##if submit is clicked
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The rersponse is")
    st.write(response) 

