#! python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:34:27 2022
@author: Tyree, Graeson

Text Broker Module
FILE NAME: TextBroker.py

COMPONENT: Utility

FUNCTION:
    -Locates text file based on the file name given
    -If there are 4 total args given, returns the tax percentage associated with the income that is >= the income given
    -If 3 total args are given, returns the corresponding error message or translated word
    -Produces error codes when:
        1) The file can't be found
        2) The wanted return cannot be found
        3) The wrong number of arguments are given
    
INPUT:
    -Parameters:
        1) File Name (with or without .txt at the end)
        2) English word, Error code, or gross income
        3) If trying to do tax calculation, add final argument (">=")
    
OUTPUT:
    Either outputs the desired correspondence of the arguments, or an error code
    

VARIABLES:
    ret - (string) Stores what will be printed
    path - (string) The path name of the Folder that stores all files
    file - (string) The name of the file that is given
    
    read - (string) The opened file
    lines - (String List) The file split into a list of Strings, based on every new line
    
    num - (float) Gross Income in
    commaInd - (int) the index of where the comma is located inside of a line of string
"""

import sys

ret = (813)
path = "TextFolder//"

file = sys.argv[1].lower()
if (file.endswith(".txt")) == False:
    file = file + ".txt"

try:
    read = open(path+file).read()
    lines = read.splitlines()
    '''
    #I had to make a separate loop for the taxes so that I could do the calculations
    #Use greater than or equal to to do tax calculations
    '''
    if len(sys.argv) == 4 and sys.argv[3] == ">=":
        num = (float)(sys.argv[2])
        '''
        If the given number is higher, give the highest tax bracket percentage
        THIS CALCULATION WORKS I PROMISE
        '''
        if num > (int)(lines[len(lines)-2][0:lines[len(lines)-2].index(",")]):
            ret = lines[len(lines)-1][lines[len(lines)-1].index(",")+1:]
            '''
            #If not in the highest tax bracket, finds the correct tax bracket percentage
            '''
        else:
            for i in range(len(lines)-1):
                commaInd = lines[i].index(",")
                if ((int)(lines[i][0:commaInd]) >= num):
                    ret = lines[i][commaInd+1:]
                    break
    #ERROR AND TRANSLATE SHOULD ONLY HAVE 3 TOTAL ARGS
    elif len(sys.argv) == 3:
        "Go Through Every Line of the File, And Return The Translation/Error"
        for line in lines:
            commaInd = line.index(",")
            if (line[0:commaInd].lower() == sys.argv[2].lower()):
                ret = line[commaInd+1:]
                break
    else:
        ret = 404
        
except:
    ret = 805903

print(ret)
    
    
