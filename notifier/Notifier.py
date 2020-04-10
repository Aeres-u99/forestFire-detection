import sys
import time
import json
import requests
if __name__ == "__main__":
    with open("/home/akuma/IOE/Notifier/code.json") as read_file:
        url = json.load(read_file)
    print(url)
    last_time = 0
    while True:
        with open("/home/akuma/IOE/ForestFire/results/SINK_16") as content_file:
            lines = content_file.readline().splitlines()
            lastline = lines[-1]
            print(lastline)
            stuffs = lastline.split(" ")
            time_interval = stuffs[0]
            coordinates = stuffs[1]
            coordinates = coordinates.split("#")
            latx = coordinates[0]
            laty = coordinates[1]
            coordinates = latx+" "+laty
            print("-----"*5)
            print(coordinates)
            if float(time_interval) > float(last_time):
                print(stuffs)
                content = "There was some issue at "+time_interval+" "+coordinates+" Kindly Take a look into it."
                print(content)
                request_url = url+"&PushTitle=Emergency&PushText="+content
                print(request_url)
                notification_status = requests.get(request_url)
                print(notification_status)
                last_time = time_interval
                time.sleep(2000)
            else:
                time.sleep(1000)


