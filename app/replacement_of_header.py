import csv
import shutil
import pandas as pd
# jadugar/wd_sku_mapping (26).csv /home/tsp/Downloads/sanfil/file-upload/csv_jadugar/wd_sku_mapping (26).csv RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
def moveFileIfNotExcel(a,b):
    source_file_path = a
    destination_file_path = "/home/tsp/Downloads/sanfil/file-upload/csv_jadugar/"+b
    print(source_file_path,destination_file_path,"RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    print(source_file_path,destination_file_path,"RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    print(source_file_path,destination_file_path,"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW##############")
    print(source_file_path,destination_file_path,"RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    print(source_file_path,destination_file_path,"RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    shutil.move(source_file_path, destination_file_path)
    print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW44444444444444444444444444444444444-----11111")

def moveFileIfNotExcelInactive(a,b):
    source_file_path = a
    destination_file_path = "/home/tsp/Downloads/sanfil/file-upload/inactiveSTARTCSV/inactive.csv"
    shutil.move(source_file_path, destination_file_path)


def headerChangeMapping(path):
    mapping=["SKU_CODE","WD_TOWN_ID","SKU_ID","ACTIVE_FLAG","MAX(B.UNIT_PRICE)","CNF_NAME","CNF_ID","WD_ID","TOWN","REGION"]
    print("Y444YY-----000000")
    
    csv_file_path = path
    print(path,"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")

    output_file_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/mapping.csv"
    data = []
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    data[0] = mapping
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Header replacement completed!")

def column_delete_wd_master(input_path , output_path):
    df = pd.read_csv(input_path)
    df = df.drop(columns=['GPI_STATE_CODE' , 'GPI_STATE' , 'ZONE_CODE' , 'ZONE' , 'WD_TOWN_CATEGORY'])
    df.to_csv(output_path, index=False)

def headerChangeMaster_user(path):
    master_user=["USER_ID","NAME","LOCATION","USER_TYPE","STATE_CODE","STATE_NAME"]			
    csv_file_path = path
    output_file_path = "/home/tsp/Downloads/sanfil/file-upload/final_jadugar/user.csv"
    data = []
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    data[0] = master_user
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Header replacement completed!")

def generate_query_wd_master(path):
    df = pd.read_csv(path)
    for index, row in df.iterrows():
        gpi_state = row["GPI_STATE"]
        zone =row["ZONE"]
        wd_id =row["WD_ID"]
        wd_normal_categary =row["WD_TOWN_CATEGORY"]
        res =f'''
UPDATE prod_db.master_wdmaster
SET gpi_state="{gpi_state}", zone="{zone}", wd_category="{wd_normal_categary}"
WHERE wd_ids ={wd_id};
        '''
    return res

def headerChangeWd_master(path):		
    wd_master=["WD_ID","WD_NAME","WD_ADDRESS1","WD_ADDRESS2","TOWN","WD_POSTAL_CODE","WD_STATE","WD_COUNTRY_ID","WD_TYPE"]
    input=path
    csv_file_path_delete = path
    output_file_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/master.csv"
    csv_file_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/master_daddy.csv"
    print("*******************************************************************************************************************************************")
    print()
    print(generate_query_wd_master(input))
    print()
    print("*******************************************************************************************************************************************")
    column_delete_wd_master(csv_file_path_delete,csv_file_path)
    data = []
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    data[0] = wd_master
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Header replacement completed!")


def headerChangeHierrachy(path):
    hierrachy=["WD_ID","WD_TOWN_ID","REGION_CODE","REGION","TOWN","TOWN_CODE","SKU_CATEGORY_CODE",'WD_TOWN_CODE']

    csv_file_path =path
    output_file_path = "/home/tsp/Downloads/sanfil/file-upload/final_jadugar/her.csv"
    data = []
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    data[0] = hierrachy
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Header replacement completed!")
