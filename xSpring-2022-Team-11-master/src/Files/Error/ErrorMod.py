"""
* Error Module
* File Name: ErrorMod.py
*
* Component: Utility
*********************************************************************************************************************
"""

"""
Project sprint 2
CMSC355 Spring 2022
Derek Yuen

"""
"""
Takes the 3 digit error code
Reads language from Option.txt
Pass parameters to text broker
Output Error Message associated with error code

"""
"""
inputs: 3 Digit Error code
outputs:MSG.txt file name


"""


"""
Variables:
DEBUGPrint - (int) Used for debugging by printing values of variables at certain times in the program.
OptionFileName - (str) The name of the file that contains the options for the program.
MSGFileName - (string) Contains the name of the file that is to be used for the message.
args - (list) Contains the arguments that are passed to the program.
sb -  (str) Contains the message that is to be sent.
out- (str) Contains the name of the file that is to be used for the output.
"""


import sys
import subprocess
import shlex

DEBUGPrint = 0 #used for debugging, checking the content of the Option.txt file.
OptionFileName = "TextFolder\\Option.txt"
MSGFileName = ""

"""
loop through the file and get the coreect error option
reads the line and strips any unncesary white space from the line
"""

with open(OptionFileName, 'r') as f:
    MSGFileName = f.readline().strip()
    
    if DEBUGPrint: #!DEBUG!#
        print("Content: ", MSGFileName, sep="",end="")


"""
calls the ServicBroker and TextBooker to pass the correct error message

"""
#The sys.argv[1] is the Error code.
args = "ServiceBroker.py" + " " + "TextBroker" + " " + MSGFileName + " " + sys.argv[1]
sb = subprocess.run(args, shell = True, stdout = subprocess.PIPE)
out = sb.stdout.strip().decode()
print(out)