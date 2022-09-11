from collections import Counter
from urllib import parse

# Read file's contents
def read_file(filename):    
    urls = []
    ip = []
    IP_DELIMITER_INDEX = 0
    URL_DELIMITER_INDEX = 6
    
    with open(filename, "r", encoding="utf_8") as f:
        for line in f.readlines():
            ip.append(line.split(" -")[IP_DELIMITER_INDEX])
            urls.append(line.split(" ")[URL_DELIMITER_INDEX])
    return ip,urls
# return number of unique ip addresses
def get_unique_ips(ip):
    return len(set(ip))

# Get top 3 most common elements in a list
def most_reccuring(list):
    counter = Counter(list)
    return counter.most_common(3)

#Get path from url
def get_paths(urls):
    paths = []
    for url in urls:
        paths.append((parse.urlsplit(url).path)) 
    return paths

#Get root of paths
def get_root(paths):
    root_paths = []
    for path in paths:
        root_paths.append(path.split("/")[1])
    return root_paths


def run_program():
    ips = []
    urls = []
    paths = []
    root_paths = []
    FILENAME = "programming-task-example-data_.log"
    
    ips, urls = read_file(FILENAME)
    print(f"There are {get_unique_ips(ips)} unique ip addresses")
    print(f"Most visited ip addresses in format (ip, frequency):\n{most_reccuring(ips)})")
    
    paths = get_paths(urls)
    root_paths = get_root(paths)
    print(f"Most visited URLs in format (path_of_url, frequency):\n{most_reccuring(root_paths)})")
    

run_program()
