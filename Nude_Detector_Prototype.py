# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:32:47 2023
Updated on Fri Apr 14 18:33:33 2023
Updated on Sat Apr 15 11:15:00 2023
Updated on Sun Apr 16 16:45:25 2023
Updated on Tue Apr 18 10:21:54 2023
@author: Victor
"""

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

# Create a function to run the selected page
def run_app():

    # Display the selected page
    page = st.sidebar.selectbox('Select a page', list(pages.keys()))
    pages[page]()

if __name__ == '__main__':
    run_app()