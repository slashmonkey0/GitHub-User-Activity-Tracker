import urllib.request
import json
username=input("Enter username: ")
request = urllib.request.urlopen(f"https://api.github.com/users/{username}/events")
data = request.read()        
data = json.loads(data)      
pushevents=0
eventrepo=set()
for event in data:
    if event["type"]=="PushEvent":
        eventrepo.add(event["repo"]["name"])
        

   
