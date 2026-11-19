import time
print(time.time())
print("starting...")
time.sleep(4)
print("finished")
currenttime=time.localtime()
print(time.strftime("%H:%M:%S"))
start=time.perf_counter()
total=sum(range(1,1000000))
end=time.perf_counter
print("total:",total)
print("execution time:",end ,start)