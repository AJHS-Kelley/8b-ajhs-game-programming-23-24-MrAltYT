# Python Performance Monitoring Module by Johnson Traevon, v0,0
import time

def execStart():
    startTime = time.time()
    return startTime

def execEnd():
    endTime = time.time()
    return endTime

def execTime(startTime, endTime):
    return f"Execution Time: {startTime - endTime} seconds.\n"
 

