# This promts user to check if they has permission to scan networks
def permission():
    print("WARNING!!! IT IS ILLEGAL TO SCAN NETWORKS YOU DO NOT HAVE PERMISSION TO. PLEASE ENSURE YOU HAVE WRITTEN, LEGAL PERMISSION TO SCAN THE TARGET NETWORK PRIOR TO PROCCEDING.")
    print("If you do not have or are unsure if you have permission please type \'False\' and this program will end.")
    userInput = input()
    return userInput

# This repromts and confirms user has permission to scan the target network
def permissionReminder():
    print("Remember to obtain legal permission to scan this network.")
    print("If you do not have permission to scan, please type \'False\'.")
    userInput = input()
    return userInput

# This parses through the scanned data for information relevent to this program.
# Returns a list of device class
def parseScannedResults(results):
    pass
    #return deviceList