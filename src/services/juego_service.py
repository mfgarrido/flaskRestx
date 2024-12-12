import random

#random genero palabra o num al azar

#funcion jurgo

def inicio():
    choices = ['Piedra','Papel','Tijera']
    player_opc = 'papel'
    opc_pc = random.choice(choices) #genero opcion al azar
    
    result = {
        "player_opc": player_opc,
        "opc_pc": opc_pc,
        "result": "ganaste" #ahora valido si esa funcion se cumple
            if(player_opc == 'papel' and opc_pc == 'piedra') else
            "perdiste" if (player_opc == "papel" and opc_pc == 'tijeras') else
            "empate"
    }
    return result