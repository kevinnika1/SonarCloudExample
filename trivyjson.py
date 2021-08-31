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
                if (v['Severity']=="UNKNOWN" or v['Severity']=="MEDIUM" or v['Severity']=="LOW"):
                    thisdict['annotation_level']="notice"
                elif (v['Severity']=="HIGH"):
                    thisdict['annotation_level']="warning"
                elif (v['Severity']=="CRITICAL"):
                    thisdict['annotation_level']="failure"
                thisdict['line']=0
                if ("Title" in v):
                    thisdict['title']=str(v.get('VulnerabilityID')+", "+v.get('Title')+", "+"Severity: "+v.get('Severity'))
                else:
                    thisdict['title']=str(v.get('VulnerabilityID')+", Severity: "+v.get('Severity'))
                result.append(thisdict)

    with open("trivyparsedresults.json", "w") as outfile:
        json.dump(result, outfile, indent=4)

except IOError:
    print("File not accessible")
