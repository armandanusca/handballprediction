import json
with open("data.txt","r"):
    data = f.readlines()[1:]
data = [{
    "name": x[0],
    "position": x[1],
    "season": x[2],
    "predictedGoals": x[3],
    "actualGoals": x[4]
} for x in data.split(",")]

with open("data.json","w") as f:
    json.dump(data, f)

