import csv

def count_rows(file_name):
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            row_count = sum(1 for row in reader)
            return row_count

    except FileNotFoundError:
        print("The file was not found")
        return 0
    
    except Exception:
        print("some error occured")
        return 0
    
if __name__ == "__main__":
    file_name = input ("Enter file name with extension: ")
    total_rows= count_rows(file_name)
    if total_rows > 0:
        print(f"total number of rows is:    {total_rows}")