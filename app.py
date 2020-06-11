from flask import Flask
from flask_restful import Api
from resources.emp import Emp, Dept

app = Flask(__name__)
api = Api(app)

api.add_resource(Emp, '/emp')
api.add_resource(Dept, '/dept')

@app.route('/')
def home():
    return("<h1 style='font-family: sans-serif;'>This is an API to interact with the EMP and DEPT tables</h1>.")

app.run(debug=True)
