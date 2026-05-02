import urllib.request
import json
class RepoTracker:
	def __init__(repoName):
		self.repoName=repoName
		self.count=0
	def countIncrease():
		self.count+=1
username=input("Enter username: ")
request = urllib.request.urlopen(f"https://api.github.com/users/{username}/events")
data = request.read()        
data = json.loads(data)      
eventrepo=set()
repoTracker=[]
for event in data:
    if event["type"]=="PushEvent":
        if event["repo"]["name"] in eventrepo:
        	
        
        else:
        eventrepo.append(RepoTracker(event["repo"]["name"]))
        

   
