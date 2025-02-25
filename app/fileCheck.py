import csv


def herValidation(path):
    csv_file_path = path
    output_file_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/herOP.csv"
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        modified_rows = []
        for row in reader:
            town = row['TOWN']
            town_code = row['TOWN_CODE']
            town_code=str(town_code)
            split_town=town.split("-")
            town_code_len=len(town_code)
            split_town_len=len(split_town[1])
            if(town_code_len!=split_town_len):
                if(town_code_len>split_town_len):
                    row['TOWN_CODE']=town_code[1:]
                else:
                    row['TOWN_CODE']="0"+town_code

            modified_rows.append(row)
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(modified_rows)

    print("Processing complete. Modified file saved at:", output_file_path)




def zeroInUserLocation(path):
    csv_file_path = path
    output_file_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/userOP.csv"
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        modified_rows = []
        for row in reader:
            location = row['LOCATION']
            if '0' not in location:
                if(len(location)>1):
                    row['LOCATION'] =location
                else:
                    row['LOCATION'] = '0' + location
            modified_rows.append(row)
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(modified_rows)

    print("Processing complete. Modified file saved at:", output_file_path)


def positionOfBlankSpaces(path):
    csv_file_path = path
    blank_space_positions = []
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row_idx, row in enumerate(reader, start=1):
            for col_idx, cell in enumerate(row, start=1):
                if cell.strip() == '':
                    blank_space_positions.append((row_idx, col_idx))
    for position in blank_space_positions:
        print("Blank space at Row:", position[0], "Column:", position[1])


def csvFileChecker(path):
    pass

#give path from final_jadugar 
def countBlankSpace(path):
    csv_file_path = path
    blank_space_count = 0
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for cell in row:
                if cell.strip() == '':
                    blank_space_count += 1
    if(blank_space_count>0):
        positionOfBlankSpaces(path)
        return False
    return True

