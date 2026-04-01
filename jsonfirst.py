import json
import csv

def json_to_csv (jdata, csv_file_name):
    #open the csv file in write mode 
    with open (csv_file_name, mode="w", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = jdata[0].keys())
        writer.writeheader()
        writer.writerows(jdata)
    
    print(f"data successfully written to {csv_file_name}")

if __name__ == "__main__":
    #json file data
    json_data = [
        {"name": "xyz", "age": 27, "city": "smthsmth"},
        {"name": "zeerpzorp", "age": 900, "city": "mars"},
        {"name": "miku", "age": "nAn", "city": "your wifi"}
    ]
    
    # Conversion
    json_to_csv(json_data, "listofnames.csv")