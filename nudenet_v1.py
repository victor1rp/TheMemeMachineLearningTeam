# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:11:11 2023

@author: Laure
"""

# Import module
from nudenet import NudeClassifier

# initialize classifier (downloads the checkpoint file automatically the first time)
classifier = NudeClassifier()

# Classify single image
image = classifier.classify('C:/male_test.jpg')
# Returns {'path_to_image_1': {'safe': PROBABILITY, 'unsafe': PROBABILITY}}
print(image)
#C:/Users/Laure/.NudeNet/Nude_classifier_test