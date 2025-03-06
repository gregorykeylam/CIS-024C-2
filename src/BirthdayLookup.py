"""
Filename: BirthdayLookup.py
Author: Gregory Lam
Created: March 5, 2025
Description: A program that help Lupe keep track of all of her friends' birthday.
"""

# Import statements
import json

# Relative path to the data file
pathToFile = "../misc/Birthday.json"

# Try to open the file specified and throw an error if it can't
try:
    jsonFile = open(pathToFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathToFile)
    print(f'ERROR: Unable to open the file "{pathToFile}"')

# Read the whole json file into a variable
birthdayList = json.load(jsonFile)

# Create an empty dictionary
birthdayDictionary = {}

# Loop through the json list and put each name and birthday into a dictionary
for elem in birthdayList:

    # Fetch name and birthday
    name = elem["name"]
    birthday = elem["birthday"]

    # Add each name and birthday into dictionary
    birthdayDictionary[name] = birthday

# Get user input
search = input("\nEnter a name to be search:  ")

# Create varibles to store results
match = {}
matchCount = 0

# Store entry that matches user input (if any) in a second dictionary 
for key in birthdayDictionary:
    # Normalize case to include both upper and lower cases during search
    if search.lower() in key.lower():
        match[key] = birthdayDictionary[key]
        # Track the number of matches
        matchCount += 1

# Print the list of birthdays if matches are found
if matchCount == 0:
    print (f'\nNone of the name matches "{search}"\n')
else:    
    print (f'\n{matchCount} friend(s) matches the name "{search}"\n')
    print ("-"*30,"     ","-"*15)
    print (f'{"Name":<30}',"     ",f'{"Birthday"}')
    print ("-"*30,"     ","-"*15)
    for key in match:
        print (f'{key:<30}',"     ",f'{match[key]}')
    print ()