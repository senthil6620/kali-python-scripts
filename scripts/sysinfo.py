import os, platform, socket, datetime
print("System:", platform.system(), platform.release())
print("Machine:", platform.machine())
print("Hostname:", socket.gethostname())
print("CPU Cores:", os.cpu_count())
print("Now:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
