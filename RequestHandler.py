import SysUtils as SU

def requestHandler(inRequest):
    
    print("input request : "+inRequest)
    result = SU.sysUtils(inRequest)
    return result

#inRequest = "uptime"
#requestHandler(inRequest)