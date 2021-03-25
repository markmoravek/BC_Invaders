import json

filename = 'highscore.json'
with open(filename, 'w') as f:
	json.dump(0, f)

print("High score has been set to 0")