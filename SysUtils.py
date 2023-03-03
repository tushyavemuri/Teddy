import time

def sysUtils(inCommand):
    print("Started processing input request "+inCommand)
    
    if(inCommand == "date"):
        print("datetime")
    elif(inCommand ==  "uptime"):
        print(time)
    elif(inCommand ==  "memory"):
            print("memory")
    elif(inCommand ==  "network"):
            print("network")
    elif(inCommand ==  "users"):
            print("users")
    elif(inCommand ==  "processes"):
            print("processes")