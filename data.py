import json
with open('data.txt','r') as f:
  players = json.load(f)

players.append({
  "name": "Armand Ioan Anusca Popa",
  "position": "Center",
  "season": "2015/2016",
  "predictedGoals": 1223,
  "actualGoals": 1242
})
