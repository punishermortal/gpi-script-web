import os
from .converter_xlsx_to_csv import excel_to_csv
from .replacement_of_header import headerChangeMapping, headerChangeMaster_user, headerChangeHierrachy, headerChangeWd_master, moveFileIfNotExcel
from .fileCheck import zeroInUserLocation, positionOfBlankSpaces, countBlankSpace, herValidation
from .uplodFile import uatUploadUser, productionUploadUser, uatUploadWdMaster, productionUploadWdMaster, uatUploadHier, productionUploadHier, productionUploadMapping, uatUploadMapping
# from insert_updateded_data import read_and_process_excel,update_database

class FileProcessor:
    def __init__(self, folder_path, csv_path, mapping_files, useR=False, uMaster=False, uHier=False, uMap=False, n=4):
    # def __init__(self, folder_path, csv_path, mapping_files, useR=True, uMaster=True, uHier=False, uMap=False, n=4):
        self.folder_path = folder_path
        self.csv_path = csv_path
        self.mapping_files = mapping_files
        self.useR = useR
        self.uMaster = uMaster
        self.uHier = uHier
        self.uMap = uMap
        self.n = n

    def filter_files(self):
        file_names = os.listdir(self.folder_path)
        return [f for f in file_names if not f.startswith(".~lock.")]
    
    def set_value_of_n(self):
        file =self.filter_files()
        if(len(file)==2):
            self.useR = True
            self.uMaster = True
            self.uHier = False
            self.uMap = False
        elif(len(file)==4):
            self.useR = False
            self.uMaster = False
            self.uHier = False
            self.uMap = False
        

    def process_files(self):
        self.set_value_of_n()
        file_names = self.filter_files()
        
        if len(file_names) == 1 and len(file_names[0]) >= 8 and file_names[0][:8] in self.mapping_files:
            self.useR = True
            self.uMaster = True
            self.uHier = True
 
        for _ in range(self.n):
            for file_name in file_names:

# wd_sku_mapping (26).csv ['wd_sku_mapping (26).csv'] 4 True True True False pppppppppppppppppppppppppp

# wd_sku_mapping (26).csv ['wd_sku_mapping (26).csv'] 4 True True True False pppppppppppppppppppppppppp



                print(file_name,file_names,self.n,self.useR , self.uMaster ,  self.uHier,self.uMap,"pppppppppppppppppppppppppp")
                if file_name.startswith("sales") and self.useR and self.uMaster and not self.uHier:
                    self.uHier = True
                    self.handle_sales_file(file_name)
                elif file_name.startswith("user") and not self.useR:
                    self.useR = True
                    self.handle_user_file(file_name)
                elif file_name.startswith("wd_m") and self.useR and not self.uMaster:
                    self.uMaster = True
                    self.handle_wd_master_file(file_name)
                elif len(file_name) >= 8 and file_name[:8] in self.mapping_files and self.uHier and self.uMaster and self.useR and not self.uMap:
                    print("YAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHAAAAAAAAAAAAAAATAK")
                    self.uMap = True
                    self.handle_mapping_file(file_name)
                print("Processed file:", file_name)
 
    def handle_sales_file(self, file_name):
        if not file_name.endswith(".csv"):
            excel_to_csv(os.path.join("jadugar", file_name), file_name)
            headerChangeHierrachy(os.path.join(self.csv_path, file_name))
            if countBlankSpace("/home/tsp/Downloads/sanfil/file-upload/final_jadugar/her.csv"):
                herValidation("/home/tsp/Downloads/sanfil/file-upload/final_jadugar/her.csv")
                output_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/herOP.csv"
                productionUploadHier(output_path)
        else:
            moveFileIfNotExcel(os.path.join("jadugar", file_name), file_name)
            headerChangeHierrachy(os.path.join(self.csv_path, file_name))
            if countBlankSpace("/home/tsp/Downloads/sanfil/file-upload/final_jadugar/her.csv"):
                herValidation("/home/tsp/Downloads/sanfil/file-upload/final_jadugar/her.csv")
                output_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/herOP.csv"
                productionUploadHier(output_path)

    def handle_user_file(self, file_name):
        if not file_name.endswith(".csv"):
            excel_to_csv(os.path.join("jadugar", file_name), file_name)
            headerChangeMaster_user(os.path.join(self.csv_path, file_name))
            if countBlankSpace("/home/tsp/Downloads/sanfil/file-upload/final_jadugar/user.csv"):
                zeroInUserLocation("/home/tsp/Downloads/sanfil/file-upload/final_jadugar/user.csv")
                output_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/userOP.csv"
                productionUploadUser(output_path)
        else:
            moveFileIfNotExcel(os.path.join("jadugar", file_name), file_name)
            headerChangeMaster_user(os.path.join(self.csv_path, file_name))
            if countBlankSpace("/home/tsp/Downloads/sanfil/file-upload/final_jadugar/user.csv"):
                zeroInUserLocation("/home/tsp/Downloads/sanfil/file-upload/final_jadugar/user.csv")
                output_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/userOP.csv"
                productionUploadUser(output_path)

    def handle_wd_master_file(self, file_name):
        # Specify the columns to store and drop
        # columns_to_store = ["GPI_STATE", "ZONE", "WD_TOWN_CATEGORY", "WD_ID"]
        if not file_name.endswith(".csv"):
            excel_to_csv(os.path.join("jadugar", file_name), file_name)
            # df, stored_data=read_and_process_excel(os.path.join(self.csv_path, file_name[:-4] + ".csv"),columns_to_store)
            headerChangeWd_master(os.path.join(self.csv_path, file_name[:-4] + "csv"))
            output_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/master.csv"
            if countBlankSpace(output_path):
                productionUploadWdMaster(output_path)
            # update_database(stored_data)
        else:
            moveFileIfNotExcel(os.path.join("jadugar", file_name), file_name)
            headerChangeWd_master(os.path.join(self.csv_path, file_name))
            output_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/master.csv"
            if countBlankSpace(output_path):
                productionUploadWdMaster(output_path)

    def handle_mapping_file(self, file_name):
        if not file_name.endswith(".csv"):
            print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIsknsjnsjxnsj")
            excel_to_csv(os.path.join("jadugar", file_name), file_name)
            headerChangeMapping(os.path.join(self.csv_path, file_name[:-4] + "csv"))
            output_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/mapping.csv"
            if countBlankSpace(output_path):
                productionUploadMapping(output_path)
        else:
            print("wwwwwwIIIIIIIIIIIIIIIIIIIIIIIIsknsjnsjxnsj",file_name)
            print("YY222YY-----000000")


            moveFileIfNotExcel(os.path.join("jadugar", file_name), file_name)
            print("YYYYYY-----000000")
            headerChangeMapping(os.path.join(self.csv_path, file_name))
            output_path = "/home/tsp/Downloads/sanfil/file-upload/fileCheck/mapping.csv"
            if countBlankSpace(output_path):
                productionUploadMapping(output_path)

# if __name__ == "__main__":
#     folder_path = "/home/tsp/Downloads/sanfil/file-upload/jadugar"
#     csv_path = "/home/tsp/Downloads/sanfil/file-upload/csv_jadugar/"
#     mapping_files = ["mortal",'Add SKU_',"WD_SKU_M", "Add_WD_S", "wd_sku_m", "wd_sku_m", "Add_WD_S", "ADD WD_S", "WD SKU M", "Wd_SKU_M", "ADD_WD_S", 'ADD WD S', "ADD WD S","Add_WD_SKU_M"]

#     processor = FileProcessor(folder_path, csv_path, mapping_files)
#     processor.process_files()

# /home/tsp/Downloads/sanfil/file-upload/file-upload/fileCheck