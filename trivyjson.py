import json

try:

    with open('trivy-results.json') as json_file:
        data = json.load(json_file)
        
        
        path=data[0]['Target']
        result= []
        if ("Vulnerabilities" in data[0]):

            for v in data[0]['Vulnerabilities']:
                thisdict= {}
                thisdict['path']=path
                thisdict['message']=str("Installed version: "+v.get('InstalledVersion')+", Fixed Version: "+v.get('FixedVersion'))
                thisdict['level']=v.get('Severity')
                if ("Title" in v):
                    thisdict['title']=str(v.get('VulnerabilityID')+", "+v.get('Title'))
                else:
                    thisdict['title']=v.get('VulnerabilityID')
                result.append(thisdict)

    with open("trivyparsedresults.json", "w") as outfile:
        json.dump(result, outfile, indent=4)

except IOError:
    print("File not accessible")
