#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:58:49 2023

@author: annetteholst
"""

import cv2
import urllib.request

# Load the image from the URL
url = "https://www.thetechoutlook.com/wp-content/uploads/2022/07/Untitled-design-9-12.jpg"
with urllib.request.urlopen(url) as url_response:
    img_array = bytearray(url_response.read())
img = cv2.imdecode(np.asarray(img_array), cv2.IMREAD_UNCHANGED)

# Blur the image
img_blurred = cv2.GaussianBlur(img, (21, 21), 0)

# Add a "Sensitive Content" filter
cv2.putText(img_blurred, "Sensitive Content", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Display the blurred image with the filter
cv2.imshow("Sensitive Content Filtered Image", img_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

