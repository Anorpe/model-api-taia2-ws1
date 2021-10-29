from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Model(Resource):
    def get(self):
        
        return "Leylisita Jaramillo"

    def post(self):


        atributo = request.json['atributo']
        

        return  {"atributo" : atributo}



@app.route('/')
def index():
  return "<h1>Bienvenido a Modelos para Tópicos Avanzados de Inteligencia Artificial 2  2021-2</h1>"

api.add_resource(Model, '/model')

if __name__ == '__main__':
     app.run_server(port='8080',debug = False)