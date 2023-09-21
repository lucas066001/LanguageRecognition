import csv
import os

MAX_CHAR = 10000
MIN_WORDS = 6

def split_and_remove_first(string):
    split_string = string.split()
    if len(split_string) > 6:
        split_string = ' '.join(split_string[1:])
    else:
        split_string = ''
    return split_string

def convert_to_csv(input_file, output_file):
    total_chars = 0
    with open(input_file,  encoding="utf8") as file:
        with open(output_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for line in file:
                str = split_and_remove_first(line.strip()).lower()
                if len(str) > MIN_WORDS and total_chars + len(str) < MAX_CHAR:
                    total_chars += len(str)
                    writer.writerow([str])
    print(total_chars)

input_file = '../Data/txt/french_prompts.txt'
output_file = '../Data/csv/FR_prompts.csv'

output_file_path = os.path.abspath(output_file)

output_directory = os.path.dirname(output_file_path)
os.makedirs(output_directory, exist_ok=True)

convert_to_csv(input_file, output_file_path)





