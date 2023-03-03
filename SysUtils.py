import time

def sysUtils(inCommand):
    print("Started processing input request "+inCommand)
    
    if(inCommand == "date"):
        return "datetime"
    elif(inCommand ==  "uptime"):
        return "uptime"
    elif(inCommand ==  "memory"):
        return "memory"
    elif(inCommand ==  "network"):
        return "network"
    elif(inCommand ==  "users"):
        return "users"
    elif(inCommand ==  "processes"):
        return "processes"