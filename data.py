import json
with open('data.txt','r') as f:
  players = json.load(f)

players += [{
  "name": "Armand Ioan Anusca Popa",
  "position": "Center",
  "season": "2015/2016",
  "predictedGoals": 1223,
  "actualGoals": 1242
},
{
  "name": "Vlad Bucur",
  "position": "Middle Wing",
  "season": "2017/2018",
  "predictedGoals": 1421,
  "actualGoals": 1231
},
{
  "name": "Vlad Ianculescu",
  "position": "Left Center",
  "season": "2015-2016",
  "predictedGoals": 1242,
  "actualGoals": 1243,
},
{
  "name": "Tuta Nora Elena",
  "position": "Left Wing",
  "season": "2017-2018",
  "predictedGoals": 1241,
  "actualGoals": 1231
}]
