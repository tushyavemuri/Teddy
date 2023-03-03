import SysUtils as SU

def requestHandler(inRequest):
    
    print("input request : "+inRequest)
    SU.sysUtils(inRequest)

inRequest = "uptime"
requestHandler(inRequest)