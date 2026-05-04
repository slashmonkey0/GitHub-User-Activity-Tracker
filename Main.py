import urllib.request
import json

username=input("Enter username: ")
request = urllib.request.urlopen(f"https://api.github.com/users/{username}/events")
data = request.read()        
data = json.loads(data)      
counter=[]
PushEventTracker=[]
for event in data:
    repo=event["repo"]["name"]
    if event["type"]=="PushEvent":
        if repo in PushEventTracker:
        	index= PushEventTracker.index(repo)
        	counter[index]+=1   	 
        else:
        	PushEventTracker.push(repo)
        	counter.push(1)

   
