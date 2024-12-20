from flask import Flask
from flask_restx import Api

from routes.juego import juego_np
from routes.pingpong import np_pingpong

from services.juego_service import inicio
from services.pingpong_service import pingpong

apirestx = Flask(__name__)
api = Api(apirestx)

api.add_namespace(juego_np,path='/juego')
api.add_namespace(np_pingpong, path='/pingpong')

if __name__=="__main__":
    apirestx.run(debug=True, host='0.0.0.0', port=5000)