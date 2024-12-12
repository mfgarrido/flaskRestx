from flask_restx import Namespace, Resource
from services.juego_service import inicio

juego_np = Namespace('juego',description='Piedra, Papel o Tijeras')


@juego_np.route('/inicio')

class inicioJuego(Resource):
    def post(self):
        return inicio(),200