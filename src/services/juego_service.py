from flask import request
import random

#random genero palabra o num al azar

#funcion jurgo


def inicio():
    opciones = ['piedra', 'papel', 'tijeras']
    choice = request.json.get('data')
    opc_pc = random.choice(opciones)
    
    resultados = {
        ('papel', 'piedra'): "ganaste",
        ('papel', 'papel'): "empate",
        ('papel', 'tijeras'): "perdiste",
        ('piedra', 'tijeras'): "ganaste",
        ('piedra', 'piedra'): "empate",
        ('piedra', 'papel'): "perdiste",
        ('tijeras', 'papel'): "ganaste",
        ('tijeras', 'tijeras'): "empate",
        ('tijeras', 'piedra'): "perdiste"
    }  

    resultado = resultados.get((choice, opc_pc), "error, elige entre piedra, papel o tijeras.")
    
    result = {
        "player_opc": choice,
        "opc_pc": opc_pc,
        "result": resultado
    }
    
    return result
    return result