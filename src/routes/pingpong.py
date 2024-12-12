from flask_restx import Namespace , Resource
from services.pingpong_service import pingpong #importamos funcion pingpong

np_pingpong = Namespace('pingpong',description="Ping Pong")

#genero la ruta
@np_pingpong.route('/')
class PingPong(Resource):
    def post(self):
        return pingpong()