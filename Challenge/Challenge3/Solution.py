#Function to get the values based on the Keys provided

def get_value_from_nested_object(obj, key):
    keys = key.split('/')
    current_obj = obj
    
    try:
        for k in keys:
            current_obj = current_obj[k]
            
        return current_obj
    except KeyError:
        return None

#Input variables 

object_input = input("Enter objects as dictionary: ")
key_input = input("Enter keys as dictionary: ")

try:
    objects = eval(object_input)
    keys = key_input
except (NameError, SyntaxError):
    print("Invalid input. Please enter valid Python dictionary format.")
    exit()

print(get_value_from_nested_object(objects, keys))
