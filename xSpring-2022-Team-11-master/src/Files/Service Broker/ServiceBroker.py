"""
* Service Broker Module
* File Name: ServiceBroker.py
*
* Component: Orchestration
*********************************************************************************************************************
* Function:
*   -Calls Services based on the passed Module name, then passes Parameters to that Module.
*   -Reads a "Service.txt" file to determine if the service exists and to find the address to that module
*   -Prints to the screen the end result of the program (Translated word, amount of tax, or error message).
*   -Also produces an error code if:
*       1)A passed service called does not exist within the service file (703).
*       2)No parameters are passed to the Service Broker (512).
*---------------------------------------------------------------------------------------------------------------------
* Input:
*   -Parameters:
*       1) Name of Service (string)
*       2) List of Parameters (string)
*
* Output
*   -Parameters:
*       1) List of Parameters sent to another Module (string).
*   -Terminal Print:
*       Prints to the screen one of three things:
*           1) An English word translated to another language.
*           2) The amount needed to be paid for taxes.
*           3) An error code along with an error message.
*---------------------------------------------------------------------------------------------------------------------
* Author: Wyatt Radican
* Version 4/26/2022 CMSC 355
*********************************************************************************************************************
"""
import sys, shlex, subprocess

"""
Variables:
DEBUGPrint - (int) Used for debugging by printing values of variables at certain times in the program.
ModuleName - (string) Contains the name of the Module that is to be called.
ParametersString - (string) Contains the Parameters that are going to be passed to the Module.
ServiceFileName - (string) Contains the name of the serivce file, this will be "Service.txt".
ModuleNameBuffer - (string) A buffer that takes the name of a service from the FileBuffer.
ModuleAddress - (string) A buffer that takes the address of a service from the FileBuffer.
TotalArgv - (int) Contains the total number of arguments passed to it.
FileBuffer - (string) a buffer that reads a line from the service file.
"""
DEBUGPrint = 0
ModuleName = str(sys.argv[1])
ParametersString = ""
ServiceFileName = "TextFolder\\Service.txt"
ModuleNameBuffer = ""
ModuleAddress = ""
TotalArgv = len(sys.argv) #Total Arguments

"""
#IGNORE:
#Some Tests to determine the directory location used by the Program and if it moves when calling another Module.
#startAddress = os.getcwd()
#startAddress = startAddress.rsplit('\\', 1)[0]
#print("Back one Address of the PROGRAM:",startAddress)
"""

if DEBUGPrint: #!DEBUG!#
    """
    A set of print() statements for debugging to see the contents of the variables: ModuleName, ServiceFileName, 
    TotalArgv, and the passed arguments (sys.argv[i]).
    """
    print("Module Name to Call:", ModuleName, sep="", end="\n")             ########################
    print("Service File Name to Read:", ServiceFileName, sep="", end="\n")  ########################
    print("Total arguments passed:", TotalArgv) ########################
    print("Parameters passed:", end = " ")  ########################
    for i in range(1, TotalArgv):
        print(sys.argv[i], end = " ") ########################

if TotalArgv - 1 >= 2:
    """
    If at least one Parameter is passed to the Service Broker.
    If DEBUGPrint is '1' then we can see if the program gets at least the Module name (sys.argv[1]) and on Parameter (sys.argv[#+1]).
    Places the Parameters in the ParametersString variable and removes the leading and trailing whitespace.
    Also inserts a quotation marks around arguments that have "<", ">", and or "=".
    """
    if DEBUGPrint: #!DEBUG!#
        print("\n2 or more arguments") ########################
       
    for i in range(2, TotalArgv):
        if ord(sys.argv[i][0]) >= 60 and ord(sys.argv[i][0]) <= 62:
            ParametersString = ParametersString + " \"" + sys.argv[i] + "\""
        else:
            ParametersString = ParametersString + " " + sys.argv[i]
    ParametersString = ParametersString.strip()

    if DEBUGPrint: #!DEBUG!#
        """
        A print() statement for debugging to see the contents of the ParameterString variable.
        """
        print(ParametersString, "\n") ########################

    with open(ServiceFileName, 'r') as f:
        """
        Opens the Service.txt file, reads a line in "FileBuffer" then splits the "FileBuffer" into its Module Name and Address.
        Checks the passed Module Name with a Service Name from the file. If they equal then it is the correct serivce then place address
        to the "ModuleAddress" string and exit loop.
        """
        for FileBuffer in f:
            #print(FileBuffer)
            ModuleNameBuffer,ModuleAddress = FileBuffer.split(',', 1)
            if ModuleName == ModuleNameBuffer:
                if DEBUGPrint: #!DEBUG!#
                    print(ModuleNameBuffer,"is",ModuleName)########################
                ModuleNameBuffer,ModuleAddress = FileBuffer.split(',', 1) #Splits the string in two with the delimiter ","
                break
                
    if not(ModuleName == ModuleNameBuffer):
        """
        If the Module name is not found then pass an Error code "703" for service not found. Then call the Service Broker to pass the Error code
        to the Error module.
        """
        if DEBUGPrint: #!DEBUG!#
            print("703 - Service Not Found") ########################
        args = "ServiceBroker.py Error 703" 
        sb = subprocess.run(args, shell = True, stdout = subprocess.PIPE)
        out = sb.stdout.strip().decode()
        print(out)
    else:
        """
        If the Module name is found then place the address and the parameters into "args" to call a module and pass the parameter list.
        """
        if DEBUGPrint: #!DEBUG!#
            print("Service Found")########################
            print("Service:",ModuleNameBuffer, end="\n")########################
            print("Address:",ModuleAddress, end='')########################
        ModuleAddress = ModuleAddress.strip()
        args = ModuleAddress + " " + ParametersString
        
        if DEBUGPrint: #!DEBUG!#
            print(args)########################

        sb = subprocess.run(args, shell = True, stdout = subprocess.PIPE)
        out = sb.stdout.strip().decode()
        print(out)
else:
    """
    If no parameters are given to the Service Broker then call the Service Broker to pass the Error code "512" to the Error module.
    """
    if DEBUGPrint: #!DEBUG!#
        print("\n512 - No Parameters Passed") ########################
    args = "ServiceBroker.py Error 512" 
    sb = subprocess.run(args, shell = True, stdout = subprocess.PIPE)
    out = sb.stdout.strip().decode()
    print(out)