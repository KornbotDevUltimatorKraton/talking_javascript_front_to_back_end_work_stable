# python
import json 
animal = {'type':'cat', 'age':12}
as_json = json.dumps(animal)

print(type(animal))  # prints '<class 'dict'>'
print(type(as_json))  # prints '<class 'str'>'

# now back again
as_object = json.loads(as_json)
print(type(as_object))  # prints '<class 'dict'>'
