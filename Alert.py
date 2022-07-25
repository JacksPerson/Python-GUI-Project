'''
Alert.py
Alert object contains functions for working with alerts in SOC operations:
        create and append alert records
        generate reimage and email texts
        find and return matching records
            investigation begun
                date/time of alert
                machine name
                User
                Username
                Agency
                supervisor
                authorizer list
                threat indicated
                source
                file path
                process path
                description
        
'''

class Alert(object):
    '''represents an Alert'''
def __init__(self, name, attribs):
    '''constructor creates Alert with a name that equals its
    creation time and date and a list containing its attributes'''
    self.name = name
    
