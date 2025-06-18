import json

#credentials = '{ "username" : ["admin", "nafis"], "password" : "password123"}'

#dict_cred = json.loads(credentials)
#print (type(dict_cred))
#print(dict_cred)
#print(dict_cred['username'][1])

#list_username = dict_cred['username']
#print(list_username[1])

with open('/Users/nazmusnafis/Desktop/API Project/credentials.json') as f:
    data = json.load(f)
    print(type(data))
    print(type(data['courses']))
    print(data['courses'][0]['id'])
    for course in data['courses']:
        #print(course['id'], course['name'])
        if course['id'] == "course-456":
            print(course['name'])
            #assert course['name'] == "Python Programming"
            assert course['name'] == "Data Structures and Algorithms"

with open('/Users/nazmusnafis/Desktop/API Project/credentials1.json') as fi:
    data_2 = json.load(fi)
    print(data == data_2)
    assert data != data_2, "Data does not match!"  # This will raise an AssertionError if the data does not match
