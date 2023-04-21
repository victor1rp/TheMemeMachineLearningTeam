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
import matplotlib.pyplot as plt
import cv2
import numpy as np

def check_nudity(image_file):
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

    # Extract nudity scores and change the type of values
    nude_classes = ["sexual_activity", "sexual_display", "erotica", "suggestive", "none"]

    # Make it actually a percentage value
    values = [nude_scores[nude_class] * 100 for nude_class in nude_classes]

    # Get index of the class with the highest percentage
    highest_percentage = max(values) 
    highest_index_value = values.index(highest_percentage)
    highest_nude_class = nude_classes[highest_index_value]
    
    return (highest_percentage, nude_classes, values, highest_nude_class)


# Home page section
# Home page section

def home():
    # Add code for home page
    st.title('Home Page')
    st.header('Prototype Nudity AI Detector')
    st.write('This app uses an AI model to detect nudity in images. Please select a page from the sidebar to get started.')
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image('https://static.independent.co.uk/s3fs-public/thumbnails/image/2012/02/24/00/25Febmodelprotest.jpg', width=400)
    
    with col2:
        st.image('https://hips.hearstapps.com/hmg-prod/images/controversial-celebrity-instagram-pics-kendall-jenner-1583441928.jpg?crop=1xw:1xh;center,top&resize=980:*', width=200)
    
    with col3:
        st.image('https://media.istockphoto.com/id/178603721/nl/foto/happy-young-couple-enjoying-summer-on-beach.jpg?s=2048x2048&w=is&k=20&c=lffSztDT4O9b_vAmpsgCr1Ij6fR6cr5tcIhtbI2SqAE=', width=300)
    
    with col4:
        st.image('https://media.istockphoto.com/id/1371786982/nl/foto/four-of-us-at-the-beach.jpg?s=2048x2048&w=is&k=20&c=otgJKBP7QHpsQ14Ctmdt0AqtnAfaE_A64zgzKJEpzxU=', width=300)

    

# User section
def user():
    # Add code for user page
    st.title('User Page')


# About section
def about():
    # Add code for user page
    st.title('About Page')
    st.header('Nudity Classes and sub-classes')
    st.write('There are 5 main Nudity Classes, each subdivided into further sub-classes. The classes are presented here in descending order of expliciteness, from the most explicit (sexual activity) down to the safest.')
    st.subheader('Sexual activity') 
    st.write('Actual or simulated sexual activity with exposed nudity.')
    st.markdown("""
    - Sexual intercourse with clear nudity, including genital-genital and oral-genital activity.
    - Clear masturbation
    - Direct touching of genitals
    - Sex toys involved in sexual activity: penetrating mouth, anus or genitals. Includes dildos, sex dolls, fleshlights, plugs.
    - Semen or vaginal fluids on faces or body parts
    """)

    st.subheader('Sexual display') 
    st.write('Explicit exposure of genitals/sexual organs')
    st.markdown("""
    - Female genitals: exposed genitalia, vulva or anus, either directly visible or through transparent, see-through or sheer clothing
    - Male genitals, male penises, both erect and non-erect, testicles, either directly visible or through transparent, see-through or sheer clothing
    - The above applies to transgender individuals
    - Sex toys not in use: dildos, sex dolls, fleshlights, butt plugs & beads
    """)

    st.subheader('Erotica') 
    st.write('Exposure of breasts, nude buttocks or the pubic region.')
    st.markdown("""
    - Nude female breasts, female breasts with visible nipples or areola
    - Nude buttocks, both male and female, in a non-sexual setting
    - Pubic region, pubic hair, female crotch region or area around genitals with no genitals visible
    """)

    st.subheader('Suggestive') 
    st.write('Situations that can be considered sexually suggestive or inappropriate, but do not include full nudity or sexual acts')
    st.markdown("""
    - Women wearing lingerie, wearing visible bras (the cup has to be visible, and sports bras are excluded), or wearing visible underwear, panties or thongs
    - Shirtless men: men where most of the area between the belly button and shoulders is visible (bare chest, topless, nude torso)
    - Suggestive cleavage / neckline, but where the areola and nipples are not visible
    - Women wearing bikinis, microbikinis or two-piece swimsuits
    """)

    st.subheader('None') 
    st.write('This class includes all cases where none of the above suggestive or explicit situations occur. As an example, this would include situations such as:')
    st.markdown("""
    - Exposed arms, legs in a non-sexual setting		
    - People hugging or making non-sexual contact
    - People kissing (mouth-mouth)
    - People wearing tank tops or stringers without nipples visible
    - Exposed back of a woman or man, if no buttocks, no genitals and no torso is visible
    - Panties, thongs, bras, swimwear shown but not worn by a person (such as on the floor)
    - Women in one-piece swimsuits
    - Underwear worn such that only the waistband is visible
    - Unclothed dolls with no sexual organs, such as Barbie dolls
    """)

# Uploading image section
def upload():
    # Add code for uploading image page
    st.title('Upload Image Page')

    st.header('Prototype Nudity AI Detector')

    # Upload image file
    image_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

    # Process uploaded image
    if image_file is not None:

        # Convert uploaded image file to numpy array
        image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Call check_nudity function to detect nudity
        highest_percentage, nude_classes, values, highest_nude_class = check_nudity(image_file)

        if (highest_nude_class == 'none' or highest_nude_class == 'suggestive') and highest_percentage > 10:
            st.image(image, caption='Uploaded Image', channels='BGR')      
        else:
            # Blur the image
            img_blurred = cv2.GaussianBlur(image, (51, 51), 0)

            # Add a "Sensitive Content" filter with a white box behind the text
            text = "Beware Nude Content"
            text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
            text_x = (image.shape[1] - text_size[0]) // 2
            text_y = (image.shape[0] + text_size[1]) // 2
            cv2.rectangle(img_blurred, (text_x-10, text_y-35), (text_x+text_size[0]+10, text_y+10), (255,255,255), -1)
            cv2.putText(img_blurred, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Create a checkbox to toggle the image blur
            blur_checkbox = st.checkbox("Unblur Image", value=True)
            if blur_checkbox:
                st.image(img_blurred, caption='Blurred Image', channels='BGR')
            else:
                st.image(image, caption='Unblurred Image', channels='BGR')

        

        # Display moderation results
        st.subheader('Moderation Results')
        st.write(f'According to the AI detector, the uploaded image contains {highest_percentage:.2f}% {highest_nude_class}')


        # Define colors for each class
        colors = ['purple', 'pink', 'red', 'yellow', 'green']

        # Style and plot the bar chart
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(8, 8))
        bars = ax.bar(nude_classes, values, label=nude_classes , color=colors)
        ax.bar_label(bars)
        plt.title('Nudity Percentage')
        plt.xlabel('Nudity Classes')
        plt.ylabel('Scores')
        plt.show()
        st.pyplot(fig)



        st.subheader('Understanding the scoring')
        st.markdown("""The scores are returned in a way that puts the emphasis on the most explicit class corresponding to the image. As an example, the class sexual_display shouldn't be understood as "is there sexual display in the image?" but rather "is there sexual display AND no sexual activity in the image?". As an illustration, an image of a woman in lingerie will score highly on the suggestive class. But if that woman is engaged in a sexual act, the AI Tool will focus on the most explicit class (sexual_activity) and return a very low score for the less explicit one (suggestive and suggestive.lingerie), because the image as a whole is explicit and should not be labelled as simply "suggestive" or "lingerie".""")

def design():
    st.title('Design')
    st.header('Design proces for our nudity detector')
    st.write("If you are interested in the proces of making this Nudity Detector you can visit our Prezi presentation for more information at: https://prezi.com/view/dQGMFpSzz8wxg2VJXKm6/")
    st.image('https://i.postimg.cc/wvJVZwLQ/Knipsel.png', width=1000)

# Create a dictionary to store the pages
pages = {
    'Home': home,
    'User': user,
    'Upload Image': upload,
    'Design': design,
    'About': about
}

# Define app title and favicon
st.set_page_config(page_title="Nudity AI Detector", page_icon=":camera:", layout="wide")

# Create a function to run the selected page
def run_app():

    # Display the selected page
    page = st.sidebar.selectbox('Select a page', list(pages.keys()))
    pages[page]()

if __name__ == '__main__':
    run_app()