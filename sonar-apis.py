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
        thisdict['path']=x['component'].replace(project+":", '')#thisdict['file']=x['component'].replace(project+":", '/')
        thisdict['title']=x.get('component')
        thisdict['message']=x.get('message')
        thisdict['level']=x.get('severity')#thisdict['annotation_level']=x.get('severity')
        for y in x['flows']:
            thisdict['line'] = {'start': y['locations'][0]['textRange']['startLine'], 'end': y['locations'][0]['textRange']['endLine']}
        for z in x['flows']:
            thisdict['raw_details']=str(z['locations'])#['locations'] 
        result.append(thisdict)
     

with open("sonarresults.json", "w") as outfile:
    json.dump(result, outfile, indent=4)
