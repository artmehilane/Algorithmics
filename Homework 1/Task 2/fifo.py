import time

fifoArray = []

def addData(data):
    fifoArray.append(data)

def removeData():
    fifoArray.pop(0)

def measureTime(n):
    start_time = time.time()
    for _ in range(n):
        addData(1)
        removeData()
    end_time = time.time()
    print(f"Input size: {n}, Time: {end_time - start_time} seconds")
        
measureTime(1000)