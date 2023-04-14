import flask 
from flask import request, jsonify
from flask_cors import CORS
import os
app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

"""Regresar un json con los datos de la carpeta public"""
@app.route('/api/publicfiles', methods=['GET'])
def publicfiles():
    #obtener los archivos de la carpeta public
    files_in_public = os.listdir('public')
    #separar nombre y extension en otro diccionario si tiene mas de un punto regresar el ultimo como extension
    for i in range(len(files_in_public)):
        file = files_in_public[i]
        if file.count('.') > 1:
            file = file.split('.')
            file_name = '.'.join(file[:-1])
            file_extension = file[-1]
        else:
            file_name, file_extension = file.split('.')
        files_in_public[i] = {
            "name": file_name,
            "extension": file_extension,
            "complete_name": file_name + "." + file_extension
        }
    #crear un json con los archivos
    json_files = jsonify(files_in_public)
    #regresar el json
    return json_files

"""Subir el archivo a la carpeta public"""
@app.route('/api/upload', methods=['POST'])
def upload():
    #obtener el archivo
    try:
        file = request.files['file']
        #guardar el archivo en la carpeta public
        file.save(os.path.join('public', file.filename))
        #regresar el nombre del archivo
        return jsonify({"name": file.filename})
    except Exception as e:
        return jsonify({"error": "No se pudo subir el archivo"})

app.run()