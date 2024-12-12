from flask import request

def pingpong():
    choice = request.json.get('choice')
    
    if choice == 'ping':
        return {'choice':'pong'}
    
    elif choice == 'pong':
        return {'choice' : 'ping'}
    
    else:
        return {'error':'debe ser ping o pong'},400