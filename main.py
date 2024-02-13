#v0.0.0

#FOSSY - Free and Open Source Voice Assistant for privacy-focused users.
#        Doesn't collect any data without users premission.
#        Ofcourse it will need data for some functions.
#        I think, knowing address to order you a pizza, is a good thing.

#Dead Brain Cells Counter: 0

#Uhh... Let's start it!

import subprocess as system
import random
import datetime as date
import time as clock
import webbrowser as web
import os
import requests
import json
#Database loading:

with open("data.json", "r") as file:
    data = json.load(file)
print(data)