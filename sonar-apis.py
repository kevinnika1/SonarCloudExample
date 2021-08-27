import requests
import json

project= "kevinnika1_SonarCloudExample"
org="kevinnika1"
query = {'organization': org, 'statuses':'OPEN', 'types':'VULNERABILITY'}
response = requests.get('https://sonarcloud.io/api/issues/search', params=query) 
issuesJSON = response.json()

result= []
for x in issuesJSON['issues']:
    if (x['project']== project):
        thisdict= {}
        thisdict['file']=x.get('component')
        thisdict['title']=x.get('component')
        thisdict['message']=x.get('message')
        thisdict['annotation_level']=x.get('severity')
        thisdict['line']=x['flows']
       # for y in x['flows']:
       #     thisdict['line']=y['locations']#['locations']
        result.append(thisdict)
     

with open("sonarresults.json", "w") as outfile:
    json.dump(result, outfile, indent=4)
