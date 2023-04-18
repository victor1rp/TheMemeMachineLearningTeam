# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 01:32:47 2023
Updated on Sat Apr 17 11:15:00 2023
@author: Victor
"""

import streamlit as st
import streamlit_authenticator as stauth


# Authentication
stauth.authenticate()

# Login/Sign Up section
def login():
    # Add code for login/sign up page
    st.write('Login/Sign Up Page')

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

        # Display moderation results
        st.subheader('Moderation Results')
        st.write(f'Nudity probability: {output["nudity"]["raw"]}')

# Create a dictionary to store the pages
pages = {
    'Login/Sign Up': login,
    'Home': home,
    'User': user,
    'Upload Image': upload
}

# Create a function to run the selected page
def run_app():
    # Check if the user is logged in, if not redirect to Login/Sign Up page
    if stauth.is_authenticated():
        # Display the selected page
        page = st.sidebar.selectbox('Select a page', list(pages.keys()))
        pages[page]()
    else:
        stauth.login('username', 'password')

if __name__ == '__main__':
    run_app()
