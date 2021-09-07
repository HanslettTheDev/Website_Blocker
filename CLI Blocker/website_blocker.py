import time
from datetime import datetime as dt
from list_of_websites import website_block_list as wbl

temp_host = "hosts"
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts" # Path to the host file on windows
# Mac Users and Linux ( hosts_path = "/etc/hosts/" )
redirect = "127.0.0.1" # Link to redirect the user when the open a page which was added to the block list
websites = wbl # Website block list

# Use a while loop to run every milli second and check the date and time

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,12) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,22):
        print("Working")
        with open(hosts_path, "r+") as file:
            hosts_content = file.read()
            for low in websites:
                if low in hosts_content:
                    pass
                else:
                    file.write(redirect + " " + low + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            hosts_content = file.readlines()
            file.seek(0)
            for hc in hosts_content:
                if not any(website in hc for website in websites):
                    file.write(hc)
            file.truncate()
        print("Gaming")

    time.sleep(5)
