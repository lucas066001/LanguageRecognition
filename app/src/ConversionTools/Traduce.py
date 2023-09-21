import csv
import deepl

AUTH_KEY = "ecc45dfe-db67-32a6-343e-3d71594712c6:fx"
FR = "FR"
TRAD_TARGET = [
    "EN-GB",
    "IT",
    "ES",
    "PT-PT",
    "DE"
]

translator = deepl.Translator(AUTH_KEY)

def traduce_into_csv(input_file, output_csv_file, desired_target_lang):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        with open(output_csv_file, 'w', newline='') as output_csv:
            csv_writer = csv.writer(output_csv)
            for row in csv_reader:
                str = "".join(row).lower()
                # Traduction ici
                str = translator.translate_text(str, target_lang=desired_target_lang, source_lang=FR)
                modified_row = [str]
                csv_writer.writerow(modified_row)


def traduce_all(tableau):
    for lang in tableau:
        input_file = '../Data/csv/FR_prompts.csv'
        output_csv_file = '../Data/csv/'+lang+'_prompts.csv'
        traduce_into_csv(input_file, output_csv_file, lang)


traduce_all(TRAD_TARGET)

