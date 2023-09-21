from collections import Counter
import csv
import string

TRAD_TARGET = [
    "FR",
    "EN-GB",
    "IT",
    "ES",
    "PT-PT",
    "DE"
]

def extract_data_from_csv(input_file, output_csv_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(output_csv_file, 'w', newline='') as output_csv:
            csv_writer = csv.writer(output_csv)
            #csv_writer.writerow(['Phrase','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','ñ','ß', 'ã', 'ç'])

            for row in csv_reader:
                str = "".join(row).lower()
                # Extraction des informations clés
                modified_row = extract_data_from_string(str)
                csv_writer.writerow(modified_row)

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


def extract_all_data(tableau):
    for lang in tableau:
        input_file = '../../assets/data/prompts/csv/'+lang+'_prompts.csv'
        output_csv_file = '../../assets/data/trainset/'+lang+'_trainset.csv'
        extract_data_from_csv(input_file, output_csv_file)


extract_all_data(TRAD_TARGET)
