from flask import Flask
from datetime import datetime
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)





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
    app.run(debug=True, use_reloader=True)

