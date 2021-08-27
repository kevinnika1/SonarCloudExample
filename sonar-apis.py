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
        thisdict['component']=x.get('component')
        thisdict['message']=x.get('message')
        thisdict['severity']=x.get('severity')
        for y in x['flows']:

            thisdict['affected-locations']=y['locations']#['locations']
            result.append(thisdict)


with open("sonarresults.json", "w") as outfile:
    json.dump(result, outfile, indent=4)
