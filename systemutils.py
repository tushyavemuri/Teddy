import time
import psutil
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
    elif(inCommand ==  "uptime"):
        logging.info(f"started")
        uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
        return f"Server uptime: {str(uptime)}"
    elif(inCommand ==  "memory"):
        logging.info(f"started")
        memory = psutil.virtual_memory()
        return f"Memory usage: {memory.percent}%"
    elif(inCommand ==  "network"):
        logging.info(f"started")
        netstat = psutil.net_connections()
        netstat_str = "Netstat:\n"
        for conn in netstat:
            netstat_str += f"{conn}\n"
        return netstat_str
    elif(inCommand ==  "users"):
        logging.info(f"started")
        users = psutil.users()
        users_str = "Current users:\n"
        for user in users:
            users_str += f"{user.name}\n"
        return users_str
    elif(inCommand ==  "processes"):
        logging.info(f"started")
        processes = psutil.process_iter()
        processes_str = "Running processes:\n"
        for proc in processes:
            processes_str += f"{proc.name()}\n"
        return processes_str
    else:
        logging.info(f"started")
        return "invalid request"