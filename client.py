import psutil
import platform
import cpuinfo
import socket

thisComputer = {}
thisComputer["cpuCount"] = psutil.cpu_count(logical=False)
thisComputer["cpuThreads"] = psutil.cpu_count()
thisComputer["platform"] = platform.uname()
thisComputer["Processor"] = cpuinfo.get_cpu_info()["brand_raw"]

print(thisComputer)

thisComputer["hostname"] = socket.gethostname()
thisComputer["IPAddr"] = socket.gethostbyname(thisComputer["hostname"])
print("Your Computer Name is: " + thisComputer["hostname"])
print("Your Computer IP Address is: " + thisComputer["IPAddr"])