import csv
import os

def read_csv_to_dict(csv_file):
    data_dict = {}
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3:  # Checking if the row has at least 3 columns
                key = row[0].strip()  # Assuming key is in the first column
                value = row[2].strip()  # Assuming text is in the third column
                data_dict[key] = value
    return data_dict

def write_docs_from_dict(data_dict, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for key, value in data_dict.items():
        doc_filename = os.path.join(output_folder, f"{key}.txt")
        with open(doc_filename, 'w') as doc_file:
            doc_file.write(value)

# Example usage:
csv_file_path = 'A2_Data.csv'  # Change this to your CSV file path
output_folder = 'dataset/review'  # Change this to the desired output folder
my_dict = read_csv_to_dict(csv_file_path)
write_docs_from_dict(my_dict, output_folder)
