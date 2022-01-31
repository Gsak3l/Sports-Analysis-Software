import filesystem_changes as fc
import json


f = open(fc.find_last_created_folder() + 'game details.json')
data = json.load(f)

print(data['Video Path'])