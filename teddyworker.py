import systemutils as SU
import logging

def teddyWorker(inRequest):
    
    logging.info(f"Input request to teddy worker : {inRequest}")
    result = SU.sysUtils(inRequest)
    return result

#inRequest = "uptime"
#requestHandler(inRequest)