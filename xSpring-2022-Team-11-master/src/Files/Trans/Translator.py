# -*- coding: utf-8 -*-
"""
Translator Module 
File Name: Translator. py

Component: Task
___________________________________________
Function: 
 Translate - The sub service broker. Determines if there is an error and
 makes an error code if so.

___________________________________________
Input: 
parameterlist; 
    the language the word is translated to, The word to be translated, 

Output:THe translated word 

___________________________________________
Author: Rose Moonjelly
Version: 04/24/2022

"""

#Import the necessary libraries and files 
import sys
import subprocess
#import shlex

"""
#variables 
wordToTrans - string; the word to be translated taken from the parameter list
translatedWord -string; final output which is the translated word
languageToTranslate- string; the language in which you eant the translated word to be
connection- the variable that acesses the other programs, like service broekr
output- 
"""
wordToTrans = ""
translatedWord = ""
"""
The languageToTranslate variable is taken from the command line 
and is converted to all lowercase letters
"""
languageToTranslate = sys.argv[1].lower()

#the words in the text files are dog, cat, brother, sister, friend, teacher
"""
Write a for loop that parses through the command line arguments (the arameters would be read like a list)
"""
for i in range(2,len(sys.argv)):
    wordToTrans = wordToTrans + sys.argv[i] + " "
    #passes the command line argument
    args = "ServiceBroker.py TextBroker" + " " + languageToTranslate + " " + sys.argv[i] 
    """
    Access the Service Broker and textbroker
    """
    connection = subprocess.run(args, shell=True, stdout= subprocess.PIPE)
    output= connection.stdout.strip().decode()
    
    """
    check to see if it is an error or find the translated word
    """
    if (output.isdigit()):
        if len(output)>3:
            errorCode = 805
        else:
            errorCode = 813
        args = "ServiceBroker.py Error " +str(errorCode)
        """
        Access error module
        """
        error = subprocess.run(args, shell = True, stdout=subprocess.PIPE)
        translatedWord = translatedWord + str(error.stdout.strip().decode()) + " "
        wordToTrans = str(errorCode)
    else:
        translatedWord = translatedWord + output + " "
"""
Output the translated word 
"""
print(wordToTrans + " - " + translatedWord )


#with open('thelangfile') as langTotransfile:
#    line = langTotransfile.readline()
#    while line:
#        line = langTotransfile.readline()
#        #loop through the lines to find input, then print the word
#        #read each line to search for a specific word the user has passed
#        #output the translated text
#        print(out)





