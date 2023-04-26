"""
Created on Tue April 26 2022
@author: Kel Raphael
TaxCalculator.py
Calculates taxes owed given income, tax year, and tax status
"""

import sys
import subprocess

owed = ""

taxYear = sys.argv[1]
status = sys.argv[2]
file = taxYear + status[0:1] + ".txt"
gross = input()

try:
    gross = round(float(gross), 2)
    args = "Service.py tb " + file + " " + (str)(gross) + "\">=\""

# call service broker -> text broker
    sb = subprocess.run(args, shell = True, stdout = subprocess.PIPE)
    out = sb.stdout.strip().decode()

# if there were no errors, value should be float; calculate tax owed
    if(str)(out).find(".") > -1:
        percent = float(sb.stdout)
        owed = round((percent * gross), 2)

# if there is error, get error output
    else:
        args = "Service.py Error 903"
        error = subprocess.run(args, shell = True, stdout = subprocess.PIPE)
        owed = error.stdout.strip().decode()

# if the input isn't a float, return 404 error
except:
    args = "Service.py Error 404"
    error = subprocess.run(args, shell = True, stdout = subprocess.PIPE)
    owed = error.stdout.strip().decode()

print(owed)