import json


candidates=[]
rows=[]

with open('data.json',"r") as f:
    data=json.load(f)
    for entry in data:
        temp={}
        temp["name"]=entry["user"]["name"]
        if "python" in entry["user"]["skills"]:
            temp["skills"]=entry["user"]["skills"]
            completed_projects=[]
            for i in entry["projects"]:
                if i["status"]=="done":
                    completed_projects.append(i["name"])
                    rows.append({'name':temp['name'],'project':i['name']})
            if completed_projects:
                temp["projects"]=completed_projects
                temp["total_projects"]=len(completed_projects)        
                candidates.append(temp)
sorted_candidates=sorted(candidates, key=lambda x: x["total_projects"], reverse=True)
with open('output.json', 'w',newline="") as f:
    json.dump(sorted_candidates,f,indent=2)
with open('row_output.json','w',newline='')as f:
    json.dump(rows,f)
