from collections import Counter
import time
from flask import Flask
import flask
from flask_cors import CORS
import os
from flask import Flask, flash, request, redirect, url_for
import joblib
import numpy as np
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploadedFiles'
CORRESPONDING_LANG = {
    "1" :"FR",
    "2" :"EN-GB",
    "3" : "IT",
    "4" : "ES",
    "5" : "PT-PT",
    "6" : "DE"
}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route("/GuessLangage")
def guess_lang():
    str = request.args.get('phrase')
    rep = test_lang(str)
    lang = CORRESPONDING_LANG[rep]
    response = flask.jsonify({'Phrase initiale': str,'Langue détectée': lang})
    return response

def test_lang(phrase):
    x = []
    model = joblib.load(open('../assets/savedModels/model.sav', 'rb'))
    ar = extract_data_from_string(phrase)
    x.append(np.array(ar))
    prediction = model.predict(np.array(x))
    return str(prediction[0])

def extract_data_from_string(str):
    str_data = []
    str_data = str_data + frequence_lettres(str)
    str_data = str_data + frequence_char_part(str)
    return str_data

def frequence_lettres(chaine):
    compteur = Counter(chaine.lower())
    longueur_chaine = len(chaine)
    tableau_frequence = [round(compteur.get(chr(i), 0) / longueur_chaine * 100, 2) for i in range(97, 123)]
    return tableau_frequence

def frequence_char_part(chaine):
    particular_chars = "ñßãç"
    compteur = Counter(chaine.lower())
    longueur_chaine = len(chaine)
    tableau_frequence = [round(compteur.get(char, 0) / longueur_chaine * 100, 2) for char in particular_chars]
    return tableau_frequence