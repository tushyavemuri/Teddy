import time
#import psutil
import os
import sys
import logging
import datetime


def sysUtils(inCommand):
    logging.info(f"Started processing input request : {inCommand}")
    if(inCommand == "date"):
        logging.info(f"started")
        now = datetime.datetime.now()
        return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"
        #return "Date"
    elif(inCommand ==  "uptime"):
        logging.info(f"started")
        uptime = os.popen('uptime -p').read()[:-1]
        return f"Server is {str(uptime)}"
        #uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
        #return f"Server uptime: {str(uptime)}"
        #return "Uptime"
    elif(inCommand ==  "memory"):
        logging.info(f"started")
        total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
        ramused = round((used_memory/total_memory) * 100, 2)
        return f"""total_memory : {total_memory}, used_memory : {used_memory}, free_memory : {free_memory} 
                    RAM memory % used: {str(ramused)}"""
        #memory = psutil.virtual_memory()
        #return f"Memory usage: {memory.percent}%"
        #return "memory"
    elif(inCommand ==  "network"):
        logging.info(f"started")
        #netstat = psutil.net_connections()
        #netstat_str = "Netstat:\n"
        #for conn in netstat:
        #    netstat_str += f"{conn}\n"
        #return netstat_str
        return "network"
    elif(inCommand ==  "users"):
        logging.info(f"started")
        # Define the structure of utmp records
        #users = psutil.users()
        #users_str = "Current users:\n"
        #for user in users:
        #    users_str += f"{user.name}\n"
        #return users_str
        return "users"
    elif(inCommand ==  "processes"):
        logging.info(f"started")
        #processes = psutil.process_iter()
        #processes_str = "Running processes:\n"
        #for proc in processes:
        #    processes_str += f"{proc.name()}\n"
        #return processes_str
        return "processes"
    else:
        logging.info(f"started")
        return "invalid request"