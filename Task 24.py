import json
 
# {key:value mapping}

a ={"name":"Ram",

   "age":21,

    "Salary":27000}
 
# conversion to JSON done by dumps() function
b = json.dumps(a)
 
# printing the output

print(b)
import json
 
# list conversion to Array

print(json.dumps(['Hi,', "Hello!", "Learners"]))
 
# tuple conversion to Array

print(json.dumps(("Hi,", "Hello!", "I'm Asvitha")))
 
# string conversion to String

print(json.dumps("Hi"))
 
# int conversion to Number

print(json.dumps(123))
 
# float conversion to Number

print(json.dumps(23.572))
 
# Boolean conversion to their respective values

print(json.dumps(True))

print(json.dumps(False))
 
# None value to null

print(json.dumps(None))