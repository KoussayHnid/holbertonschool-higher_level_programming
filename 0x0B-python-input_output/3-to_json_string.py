#!/usr/bin/python3
'''function that returns the JSON 
representation of an object (string)'''
def to_json_string(my_obj):
    '''
    you don’t need to manage exceptions if the object can’t be serialized.
    '''
    return json.dumps(my_obj)
