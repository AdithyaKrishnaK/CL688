import csv
from tqdm import tqdm

def toCSV(input_file, output_file, headings):
    feature_headings = [f"feature{i}" for i in range(16)]

    with open(input_file, 'r') as text_file, open(output_file, 'w', newline='') as csv_file:
        next(text_file)

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headings + feature_headings)
        for line in tqdm(text_file):
            fields = line.strip().split(' ') 
            csv_writer.writerow([field for field in fields if field!=""])

    print(f"Conversion from {input_file} to {output_file} is complete.")

toCSV("data/ethylene_CO.txt","proc_data/ethylene_CO.csv",['Time','Conc_CO','Conc_Eth'])