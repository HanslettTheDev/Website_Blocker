host_temp = "hosts"
text_file = 'site.txt'
redirect = "127.0.0.1"


def add_website_to_txt(website_link):
    print('from utils', website_link)
    if website_link == "":
        print('error')    
    else:
        with open(text_file, 'a') as f:
            f.write(website_link)
            f.write('\n')
    text = {
    "message": "File successfully added"
    }
    return text
    

def run_blocker():
    with open('site.txt', 'r') as f:
        global websites 
        websites = f.readlines()
    with open(host_temp, "r+") as file:
        hosts_content = file.read()
        for low in websites:
            if low in hosts_content:
                pass
            else:
                file.write(redirect + " " + low)
    text = {
    "message": "Blocker is running successfully! Close all active browsers and launch again for the script to take effect"
    }
    return text
    
def stop_blocker():
    with open(host_temp, 'r+') as file:
        hosts_content = file.readlines()
        file.seek(0)
        for hc in hosts_content:
            if not any(website in hc for website in websites):
                file.write(hc)
        file.truncate()
    text = {
    "message": "Blocker has been stopped! Close all active browsers to be able to view the blocked sites"
    }
    return text
