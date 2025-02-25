import pandas as pd
def excel_to_csv(rasta,a):
    print("jjjjj     2")
    excel_file_path = rasta
    csv_file_path = "/home/tsp/Downloads/sanfil/file-upload/csv_jadugar/"+a[:len(a)-4]+"csv"
    data_frame = pd.read_excel(excel_file_path)
    data_frame.to_csv(csv_file_path, index=False)
    print("Conversion from Excel to CSV completed!")
# excel_to_csv("/home/tsp/Downloads/sanfil/file-upload/WD_SKU_Mapping.xlsx","WD_SKU_Mapping.xlsx")

def excel_to_csvINACTIVE(rasta,a):
    excel_file_path = rasta
    csv_file_path = "/home/tsp/Downloads/sanfil/file-upload/inactiveSTARTCSV/inactive.csv"
    data_frame = pd.read_excel(excel_file_path)
    data_frame.to_csv(csv_file_path, index=False)
    print("Conversion from Excel to CSV completed!")