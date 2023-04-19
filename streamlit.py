# -*- coding: utf-8 -*-

import requests
import json
import streamlit as st

# Define API credentials and parameters
API_USER = '928209'
API_SECRET = 'fbJieoTnWSSCqmKbgbmU'
API_PARAMS = {'models': 'nudity-2.0', 'api_user': API_USER, 'api_secret': API_SECRET}

# Function to check nudity in an image using the Sightengine API
def check_nudity(image_file):
    files = {'media': image_file}
    r = requests.post('https://api.sightengine.com/1.0/check.json', files=files, data=API_PARAMS)
    return json.loads(r.text)

# Home page section
def home():
    # Add code for home page
    st.write('Home Page')

# User section
def user():
    # Add code for user page
    st.write('User Page')


# Uploading image section
def upload():
    # Add code for uploading image page
    st.write('Upload Image Page')
    st.title('Prototype Nudity AI Detector')

    # Upload image file
    image_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

    # Process uploaded image
    if image_file is not None:
        # Display uploaded image
        st.image(image_file, caption='Uploaded Image', use_column_width=True)

        # Call SightEngine API to detect nudity
        files = {'media': image_file.getvalue()}
        params = {
            'models': 'nudity-2.0',
            'api_user': '928209',
            'api_secret': 'fbJieoTnWSSCqmKbgbmU'
        }
        response = requests.post('https://api.sightengine.com/1.0/check.json', files=files, data=params)

        # Process API response
        output = json.loads(response.text)
        nude_scores = output['nudity']
        nude_classes = ["sexual_activity", "sexual_display", "erotica", "suggestive", "none"]


        # Display moderation results
        st.subheader('Moderation Results')
        st.write(f'Nudity probability: {nude_scores}')

# Create a dictionary to store the pages
pages = {
    'Home': home,
    'User': user,
    'Upload Image': upload
}

# Define app title and favicon
st.set_page_config(page_title="Prototype Nudity AI Detector", page_icon=":guardsman:", layout="wide")

# Add title and description txt kan aangepast worden
st.title('Prototype Nudity AI Detector')
st.write('This app uses an AI model to detect nudity in images. Please select a page from the sidebar to get started.')

# Create a function to run the selected page
def run_app():

    # Display the selected page
    page = st.sidebar.selectbox('Select a page', list(pages.keys()))
    pages[page]()

if __name__ == '__main__':
    run_app()
