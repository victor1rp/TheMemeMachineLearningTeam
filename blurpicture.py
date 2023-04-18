#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:43:25 2023

@author: annetteholst
"""

from PIL import Image, ImageFilter
import requests
from io import BytesIO

# Download the image from the URL
url = "https://www.thetechoutlook.com/wp-content/uploads/2022/07/Untitled-design-9-12.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Apply the blur effect
blurred_img = img.filter(ImageFilter.GaussianBlur(radius=10))

# Save the blurred image
blurred_img.save("blurred_image.jpg")



