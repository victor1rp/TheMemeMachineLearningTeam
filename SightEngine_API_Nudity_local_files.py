# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:59:19 2023

@author: Laurens
"""

# this example uses requests
import requests
import json

params = {
  'models': 'nudity-2.0',
  'api_user': '928209',
  'api_secret': 'fbJieoTnWSSCqmKbgbmU'
}
files = {'media': open('/full/path/to/image.jpg', 'rb')}
r = requests.post('https://api.sightengine.com/1.0/check.json', files=files, data=params)

output = json.loads(r.text)