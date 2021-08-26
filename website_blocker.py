import time
from datetime import datetime as dt

temp_host = "hosts"
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts" # Path to the host file on windows
redirect = "127.0.0.1" # Link to redirect the user when the open a page which was added to the block list
list_of_websites = ["www.facebook.com", "www.gmail.com"] # Website block list

# Use a while loop to run every milli second and check the date and time

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,7) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working")
        with open(temp_host, "r+") as file:
            hosts_content = file.read()
            for low in list_of_websites:
                if low in hosts_content:
                    pass
                else:
                    file.write(redirect + " " + low + "\n")
    else:
        print("Gaming")
        with open(temp_host, "r+") as file:
            hosts_content = file.readlines()
            for hc in hosts_content:
                if not any(low in hc for low in list_of_websites):
                    file.write(hc)

    time.sleep(5)
