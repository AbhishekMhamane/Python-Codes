user = '''[{"name" : "abhsihek","mob" : "1234"},
{"name" : "mahesh","mob" : "1234"}]'''

import json 
data = json.loads(user)
result = json.dumps(data,indent=4)
print(result)