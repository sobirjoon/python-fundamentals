# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 14:41:06 2022

@author: sobirjon
"""

import webbrowser
import json
from urllib.request import urlopen

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20120212: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)

response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)

try: 
    old_site = data["archived_snapshots"] ["closest"] ["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now")
    webbrowser.open(old_site)

except:
    print("Sorry, no luck finding", site)