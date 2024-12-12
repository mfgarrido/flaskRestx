from flask import request
import random

#random genero palabra o num al azar

#funcion jurgo


def inicio():
    choices = ['Piedra','Papel','Tijera']
   # player_opc = 'papel'
    choice = request.json.get('data')
    opc_pc = random.choice(choices) #genero opcion al azar
    
    result = {
        "player_opc": choice,
        "opc_pc": opc_pc,
        "result": "ganaste" #ahora valido si esa funcion se cumple
            if choice == 'papel' and opc_pc == 'piedra' else
            "perdiste" if choice == "papel" and opc_pc == 'tijeras' else
            "empate"

            if choice == 'piedra' and opc_pc == 'tijeras' else
            "perdiste" if choice == "piedra" and opc_pc == 'papel' else
            "empate"
            
            if choice == 'tijeras' and opc_pc == 'papel' else
            "perdiste" if choice =="tijeras" and opc_pc =='piedra'  else
            "empate"
    }
    return result