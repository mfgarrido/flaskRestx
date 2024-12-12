from flask import request
import random

#random genero palabra o num al azar

#funcion jurgo


def inicio():
    opciones = ['piedra', 'papel', 'tijeras']
    choice = request.json.get('data')
    opc_pc = random.choice(opciones)
    
    if choice == 'papel' and opc_pc == 'piedra':
        resultado = "ganaste"
    elif choice == 'papel' and opc_pc == 'tijeras':
        resultado = "perdiste"
    elif choice == 'papel' and opc_pc == 'papel':
        resultado = "empate"

    elif choice == 'piedra' and opc_pc == 'tijeras':
        resultado = "ganaste"
    elif choice == 'piedra' and opc_pc == 'papel':
        resultado = "perdiste"
    elif choice == 'piedra' and opc_pc == 'piedra':
        resultado = "empate"
        
    elif choice == 'tijeras' and opc_pc == 'papel':
        resultado = "ganaste"
    elif choice == 'tijeras' and opc_pc == 'piedra':
        resultado = "perdiste"
    elif choice == 'tijeras' and opc_pc == 'tijeras':
        resultado = "empate"
    
    else:
        resultado = "error ,elige entre piedra, papel o tijeras."
    
    result = {
        "player_opc": choice,
        "opc_pc": opc_pc,
        "result": resultado
    }
    
    return result