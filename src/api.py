from dataclasses import dataclass
import time
from src.utils import add_website_to_txt, run_blocker, stop_blocker

@dataclass
class API:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def saveTextToTextFile(self, website_link):
        print('Web link', website_link)
        website_link = website_link
        response = add_website_to_txt(website_link)
        return response
    
    def runWebsiteBlocker(self):
        response = run_blocker()
        return response

    def stopWebsiteBlocker(self):
        response = stop_blocker()
        return response
    
    def triggerJs(self):
        print('trigger is working')
        print('run some long process')
    
    def cancelHeavyStuff(self):
        time.sleep(0.1)
        self.cancel_heavy_stuff_flag = True