# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:53:23 2023

@author: Laurens

API Source: https://dashboard.sightengine.com/getstarted
30-Day free trial
"""

# this example uses requests
import requests
import json
import matplotlib.pyplot as plt

#insert image URL, see end of page for collected links
params = {
  'url': 'https://www.malemodelscene.net/wp-content/uploads/2020/02/Useful-Tips-for-Improving-Your-Career-as-a-Male-Model-2.jpg',
  'models': 'nudity-2.0',
  'api_user': '928209',
  'api_secret': 'fbJieoTnWSSCqmKbgbmU'
}
r = requests.get('https://api.sightengine.com/1.0/check.json', params=params)

#output = json.loads(r.text)
#print(output)

#This code checks for errors by examining the status code of the API response, and prints out the response text if there is an error 
#or if the status code is OK (200). The json.dumps(output, indent=2) line formats the JSON output for easier reading by humans.

if r.status_code == 200:
    output = json.loads(r.text)
    print(json.dumps(output, indent=2))
else:
    print(f"Error: {r.status_code}")
    print(r.text)
    
# Extract nudity scores
nude_scores = output['nudity']
nude_classes = ["sexual_activity", "sexual_display", "erotica", "suggestive", "none"]
values = [nude_scores[nude_class] for nude_class in nude_classes]
labels = nude_classes
# Rotate the x-labels by 30 degrees, and keep the text aligned horizontally
plt.xticks(rotation=30, horizontalalignment="center")
# Define colors for each class
colors = ['blue', 'green', 'red', 'yellow', 'purple']

# Plot the bar chart
plt.bar(nude_classes, values, color=colors)

plt.title('Nudity Scores')
plt.xlabel('Nude Class')
plt.ylabel('Score')
plt.show()


'''
Test Images:
    
1. Female rights activists (naked upper bodies) 
    https://static.independent.co.uk/s3fs-public/thumbnails/image/2012/02/24/00/25Febmodelprotest.jpg
    
2. Playmate of the year 2020 (full nude)
    https://p4k7u4x7.ssl.hwcdn.net/content/models_ret/1802-stella-tiana-stegmann_400.jpg
    
3. Male Model in shorts
    https://www.malemodelscene.net/wp-content/uploads/2020/02/Useful-Tips-for-Improving-Your-Career-as-a-Male-Model-2.jpg   
'''