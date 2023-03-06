import linuxsystemutils as LSU
import windowssystemutils as WSU
import logging

def teddyWorker(inRequest):
    
    logging.info(f"Input request to teddy worker : {inRequest}")
    result = LSU.sysUtils(inRequest)
    return result

#inRequest = "uptime"
#requestHandler(inRequest)