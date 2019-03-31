import json
with open('data.txt','r') as f:
  players = json.load(f)

players += [{
  "name": "Armand Ioan Anusca Popa",
  "position": "Line Player",
  "season": "2015/2016",
  "predictedGoals": 3.24,
  "actualGoals": 3.42
},
{
  "name": "Vlad Bucur",
  "position": "Line Player",
  "season": "2017/2018",
  "predictedGoals": 4.3,
  "actualGoals": 3.78
},
{
  "name": "Vlad Ianculescu",
  "position": "Left Back",
  "season": "2015/2016",
  "predictedGoals": 2.78,
  "actualGoals": 1.2,
},
{
  "name": "Nora Elena Tuta",
  "position": "Left Wing",
  "season": "2017/2018",
  "predictedGoals": 8.3,
  "actualGoals": 7.9
}]
