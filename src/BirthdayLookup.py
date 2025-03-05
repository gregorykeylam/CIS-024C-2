"""
Filename: HelloWorld.py
Author: Gregory Lam
Created: March 2, 2025
Description: A program that prints "hello world" and python version it is running on.
"""


import json

#
# this is a relative path to the .json data file
# you can also use a "full" or "absolute path" to the file
# windows and mac paths are different.  You should google and youttube to learn about paths if you are
# not familiar with them.  They are important fundamental computer concepts.
#
# this is a full windows path, note the forward slashes "/" used in python
# pathToFile = "E:/Users/jerome/GitHub/evc-cit134a-python/birthday/birthday.json"
#
# mac (which is built on linux) and linux paths are like this: "a/b/c/d/e/f.json"
#

# relative path
pathToFile = "./src/Birthday.json"


# try to open a file and throw a error if it is not found
try:
    jsonFile = open(pathToFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathToFile)


# read the whole json file into a variable
birthdayList = json.load(jsonFile)

# create an empty dictionary
birthdayDictionary = {}

# loop json list of data and put each name and birthday into a dictionary
for elem in birthdayList:

    # fetch name and birthday
    name = elem["name"]
    birthday = elem["birthday"]

   #print("name = " + name)
   #print("birthday = " + birthday)
 
    birthdayDictionary[name] = birthday


# to print a value in the dictionary by giving it a string with the name as the key
#print("Jocelyn Jones's birthday is: " + birthdayDictionary["Jocelyn Jones"])

# to get user input

search = input("\nEnter a name to be search:  ")

Match = {}
MatchCount = 0

for key in birthdayDictionary:
    if search.lower() in key.lower():
        Match[key] = birthdayDictionary[key]
        MatchCount += 1

if MatchCount == 0:
    print (f'\nNone of the name matches "{search}"\n')
else:    
    print (f'\n{MatchCount} friend(s) matches the name "{search}"\n')
    print ("-"*30,"     ","-"*15)
    print (f'{"Name":<30}',"     ",f'{"Birthday"}')
    print ("-"*30,"     ","-"*15)
    for key in Match:
        print (f'{key:<30}',"     ",f'{Match[key]}')
    print ()