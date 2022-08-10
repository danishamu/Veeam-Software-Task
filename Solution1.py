import os
import psutil
  
# Getting loadover20 minutes
load1, load5, load20 = psutil.getloadavg()
  
cpu_usage = (load20/os.cpu_count()) * 100
  
print("The CPU usage is : ", cpu_usage)

# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])

# folder path
dir_path = r'c:\Users\Danish Iqbal'
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)
