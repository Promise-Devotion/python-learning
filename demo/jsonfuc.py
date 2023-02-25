import json

person_dict = {'first': 'Sijun', 'last': 'Yanni'}

language_list = ['CSharpe', 'python', 'Javascript']
person_dict['language'] = language_list
person_item = json.dumps(person_dict)
print(person_item)