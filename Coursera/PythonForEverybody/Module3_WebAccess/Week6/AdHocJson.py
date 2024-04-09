import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : { 
        "hide" : "yes"
    }
    }  
'''

info = json.loads(data)
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])

# now to a list
input2 = '''[
    {   "id" : "001",
        "x" : "2",
        "name" : "Matt"
    },
        {   "id" : "009",
        "x" : "7",
        "name" : "Tim"
    }
]
'''
info2 = json.loads(input2)
print('User count: ', len(info2))
for item in info2:
    print('Name: ',item['name'])
    print('Id: ', item['id'])
    print('Attribute: ', item['x'])

# www.geoapify.com
# Forward Geocoding API -- takes that address and finds the GPS coordinates
# All you need is an API key
# http://py4e-data.dr-chuck.net/opengeo?q=Ann+Arbor%2C+MI

# friends = ["Glenn", "Sally", "Jen"]
# info3 = json.loads(friends)
# print('Info 3....')
# print(info3)               
    