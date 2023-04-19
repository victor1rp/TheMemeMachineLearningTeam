#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:51:54 2023

@author: annetteholst
"""
import cv2
import urllib.request
import numpy as np

# Load the image from the URL
url = "https://assets.rebelmouse.io/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbWFnZSI6Imh0dHBzOi8vYXNzZXRzLnJibC5tcy8xODkyNjY3Ni9vcmlnaW4uanBnIiwiZXhwaXJlc19hdCI6MTY5MjEzOTU4NH0.lfxouvS-K7iY15RrixmnbDwL-CucLF12rMb7fYU9r-U/img.jpg?width=730&quality=80"
with urllib.request.urlopen(url) as url_response:
    img_array = bytearray(url_response.read())
img = cv2.imdecode(np.asarray(img_array), cv2.IMREAD_UNCHANGED)

# Blur the image more
img_blurred = cv2.GaussianBlur(img, (51, 51), 0)

# Add a "Sensitive Content" filter with a white box behind the text
text = "Beware Nude Content"
text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
text_x = (img.shape[1] - text_size[0]) // 2
text_y = (img.shape[0] + text_size[1]) // 2
cv2.rectangle(img_blurred, (text_x-10, text_y-35), (text_x+text_size[0]+10, text_y+10), (255,255,255), -1)
cv2.putText(img_blurred, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Save the blurred image to a file
cv2.imwrite("blurred_image.jpg", img_blurred)

# Display the blurred image with the filter
cv2.imshow("Sensitive Content Filtered Image", img_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()



