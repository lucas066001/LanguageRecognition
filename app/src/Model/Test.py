from collections import Counter
import joblib
import numpy as np


def test_lang(phrase):
    x = []
    model = joblib.load(open('../../assets/savedModels/model.sav', 'rb'))
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

test_lang("Hallo, wie geht es euch, meine morgendlichen Freunde")