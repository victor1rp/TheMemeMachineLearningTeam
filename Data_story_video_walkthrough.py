# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:34:03 2023

@author: Victor
"""

import pandas as pd

# Load the shark attacks data
attacks = pd.read_excel("C:/Users/victo/.spyder-py3/Data_story_video_walkthrough/shark_attacks.xlsx")

# Subsetting the data without unnecessary columns
shark_attacks_sub = attacks.drop(columns=['Case Number', 'Location', 'Name', 'Investigator or Source', 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2',
'original order', 'Unnamed: 22', 'Unnamed: 23'])

# Remove rows with null values
shark_attacks = shark_attacks_sub[shark_attacks_sub['Year'] >= 2000]

# Group the data by fatal attacks and count the number of attacks
fatal_attacks = shark_attacks.groupby(['Fatal (Y/N)']).size().reset_index(name='Attacks')

# Load the gross import shark fin data
gross_import = pd.read_excel(r'C:\Users\victo\.spyder-py3\Data_story_video_walkthrough\gross_import.xlsx')

# Load the country code data
country_code = pd.read_excel(r'C:\Users\victo\.spyder-py3\Data_story_video_walkthrough\country_code.xlsx')

# Create a dictionary to map country codes to country names
country_code_name = dict(zip(country_code['Code Value'], country_code['Country']))

# Replace the Importer, Exporter, and Origin columns with their corresponding country names
gross_import['Importer'] = gross_import['Importer'].map(country_code_name)
gross_import['Exporter'] = gross_import['Exporter'].map(country_code_name)
gross_import['Origin'] = gross_import['Origin'].map(country_code_name)

# Group the data by year and exporter country and calculate the total amount of shark fin traded
gross_import_by_year_exporter = gross_import.groupby(['Year', 'Exporter'])['Exporter reported quantity'].sum().reset_index()

# Group the data by year and importer country and calculate the total amount of shark fin traded
gross_import_by_year_importer = gross_import.groupby(['Year', 'Importer'])['Importer reported quantity'].sum().reset_index()

# Replace the letters in the Purpose column with their corresponding words
gross_import["Purpose"].replace({
    "E": "Educational",
    "L": "Law Enforcement/Judicial/Forensic",
    "P": "Personal",
    "Q": "Circus and Travelling Exhibitions",
    "S": "Scientific",
    "T": "Commercial"
}, inplace=True)

# Replace the letters in the Source column with their corresponding words
gross_import["Source"].replace({
    "C": "Captive-bred Animals",
    "I": "Confiscations/Seizures",
    "O": "Pre-Convention",
    "W": "Wild",
    "X": "Specimens taken in the marine environment not under the jurisdiction of any State"
}, inplace=True)


# Save the updated gross_import DataFrame as an Excel file
gross_import.to_excel("C:/Users/victo/.spyder-py3/Data_story_video_walkthrough/gross_import_updated.xlsx", index=False)

shark_attacks.to_excel("C:/Users/victo/.spyder-py3/Data_story_video_walkthrough/shark_attacks_updated.xlsx", index=False)

# Save the attacks by country,species,activity,injury and fatal in new sheets in the "shark_attacks_updated.xlsx" file
with pd.ExcelWriter("C:/Users/victo/.spyder-py3/Data_story_video_walkthrough/shark_attacks_updated.xlsx", engine='openpyxl', mode='a') as writer:
    fatal_attacks.to_excel(writer, sheet_name='Fatal Attacks', index=False)
    
    
with pd.ExcelWriter("C:/Users/victo/.spyder-py3/Data_story_video_walkthrough/gross_import_updated.xlsx", engine='openpyxl', mode='a') as writer:
    gross_import_by_year_exporter.to_excel(writer, sheet_name='Traded by Year and Exporter', index=False)
    gross_import_by_year_importer.to_excel(writer, sheet_name='Traded by Year and Importer', index=False)