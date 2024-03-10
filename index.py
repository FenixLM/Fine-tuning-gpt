from flask import Flask, jsonify
from controllers.fine_tuning_controller import fineTuningController

app = Flask(__name__)
fine_Tuning_controller = fineTuningController()

@app.route('/')
def index():
    return 'Hola Mundo!'

# primero damos formato al archivo (nuestro JSON con los ejemplos)
@app.route('/format-file', methods=['GET'])
def format_file():
    data = fine_Tuning_controller.format_file()
    return jsonify(data)

# cargamos la data a los servidores de OpenIA
@app.route('/charge-data', methods=['GET'])
def charge_data():
    data = fine_Tuning_controller.charge_data()
    return jsonify(data)

# Creamos nuestro nuevo modelo de trabajo
@app.route('/create-job', methods=['GET'])
def create_fine_tunig_job():
    data = fine_Tuning_controller.create_fine_tunig_job()
    return jsonify(data)

# Probamos nuestro nuevo modelo
@app.route('/test-job', methods=['GET'])
def test_fine_tuning():
    data = fine_Tuning_controller.test_fine_tuning()
    return jsonify(data)





