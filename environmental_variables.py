import os
import pprint
environmental_variables=os.environ
pprint.pprint(dict(environmental_variables), width = 2)
print(os.environ.get('USERNAME'))
