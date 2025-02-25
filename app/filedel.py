import os

class DirectoryCleaner:
    def __init__(self, folder_paths):
        """
        Initializes the DirectoryCleaner with a list of folder paths.

        Parameters:
        folder_paths (list of str): The paths of the directories to clear.
        """
        self.folder_paths = folder_paths

    def clear_directory(self, folder_path):
        """
        Clears all files in the specified directory.

        Parameters:
        folder_path (str): The path of the directory to clear.
        """
        if not os.path.exists(folder_path):
            print(f"Directory '{folder_path}' does not exist.")
            return

        file_names = os.listdir(folder_path)
        for file_name in file_names:
            file_path = os.path.join(folder_path, file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_name}' deleted successfully from '{folder_path}'.")
            else:
                print(f"File '{file_name}' does not exist in '{folder_path}'.")

    def clean_all_directories(self):
        """
        Clears all files in the predefined directories.
        """
        for folder_path in self.folder_paths:
            self.clear_directory(folder_path)

def dele():
    folder_paths = [
        "/home/tsp/Downloads/sanfil/file-upload/csv_jadugar",
        "/home/tsp/Downloads/sanfil/file-upload/fileCheck",
        "/home/tsp/Downloads/sanfil/file-upload/final_jadugar",
        "/home/tsp/Downloads/sanfil/file-upload/jadugar",
        "/home/tsp/Downloads/sanfil/file-upload/productionRemark",
        "/home/tsp/Downloads/sanfil/file-upload/uatRemark",
        "/home/tsp/Downloads/sanfil/file-upload/inactiveSTART",
        "/home/tsp/Downloads/sanfil/file-upload/inactiveSTARTCSV",
        "/home/tsp/Downloads/sanfil/file-upload/prodInactiveRemark",
        "/home/tsp/Downloads/sanfil/file-upload/uatInactiveRemark",
        "/home/tsp/Downloads/sanfil/file-upload/loginReportCal",
        "/home/tsp/Downloads/sanfil/file-upload/panmapping"
    ]

    cleaner = DirectoryCleaner(folder_paths)
    cleaner.clean_all_directories()