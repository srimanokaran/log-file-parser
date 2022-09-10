import collections
from urllib import parse
# set of unique ip addresses
ip = []
# list of urls
urls = []
with open("programming-task-example-data_.log", "r", encoding="utf_8") as f:
    for line in f.readlines():
        ip.append(line.split(" -")[0])
        urls.append(line.split(" ")[6])
    
#1. Find number of unique ip addresses
print(f"Number of unique ip addresses: {len(set(ip))}\n")

#3. 
counter = collections.Counter(ip)
print(f"Top 3 most active ip-addresses, in the format of (ip address, frequency):\n{counter.most_common(3)}" )
        

#1. The number of unique IP addresses
# print(f"Unique ip addresses in the log: {len(ip)}")