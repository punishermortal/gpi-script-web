from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
from django.http import FileResponse, JsonResponse,Http404
from pathlib import Path
from .read_file_name import FileProcessor
from .filedel import dele

def upload_form(request):
    return render(request, 'app/upload.html')

def mapping_script():
    folder_path = "/home/tsp/Downloads/sanfil/file-upload/jadugar"
    csv_path = "/home/tsp/Downloads/sanfil/file-upload/csv_jadugar/"
    mapping_files = ["mortal",'Add SKU_',"WD_SKU_M", "Add_WD_S", "wd_sku_m", "wd_sku_m", "Add_WD_S", "ADD WD_S", "WD SKU M", "Wd_SKU_M", "ADD_WD_S", 'ADD WD S', "ADD WD S","Add_WD_SKU_M"]
    processor = FileProcessor(folder_path, csv_path, mapping_files)
    processor.process_files()
    return "abhijeet"

@csrf_exempt  # Disable CSRF for testing; in production, configure CSRF tokens properly
def upload_file(request):
    if request.method == 'POST' and len(request.FILES) > 0:
        # Dictionary to store the upload results for each file
        upload_results = {}

        # Iterate over the files sent with the request
        for file_key, uploaded_file in request.FILES.items():
            # Define the path where the file will be saved (ensure the directory exists)
            file_path = os.path.join('/home/tsp/Downloads/sanfil/file-upload/jadugar', uploaded_file.name)
            # Save each file in chunks to avoid memory issues with large files
            try:
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
                upload_results[file_key] = f"File {uploaded_file.name} uploaded successfully!"
                mapping_script()
            except Exception as e:
                upload_results[file_key] = f"Error uploading {uploaded_file.name}: {str(e)}"
        try:
            print(mapping_script())
            print("IIIIIIIIIIIII")
        except Exception as e:
            pass
        return JsonResponse({'message': 'File upload results', 'results': upload_results})
    else:
        return JsonResponse({'error': 'No files provided or invalid request.'}, status=400)



def download_all_files(request):
    folder_path = '/home/tsp/Downloads/sanfil/file-upload/productionRemark'
    print("Downloading all files from:", folder_path)

    # Check if the folder exists
    if not os.path.exists(folder_path):
        return JsonResponse({'error': 'Folder not found'}, status=404)

    # Get the list of files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        return JsonResponse({'error': 'No files found in the folder'}, status=404)

    # Create a generator to serve each file one after the other
    def file_generator():
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    yield f.read()

    response = FileResponse(file_generator(), content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="files.csv"'  # Change this filename as necessary

    return response



def csv_file_list(request):
    # Specify the folder where your CSV files are located
    folder_path = Path("/home/tsp/Downloads/sanfil/file-upload/productionRemark")
    
    # Get a list of CSV files in the folder
    csv_files = [str(file.name) for file in folder_path.glob("*.csv")]

    # Render the HTML template and pass the CSV file names to it
    return render(request, 'app/csv_list.html', {'csv_files': csv_files})



def download_csv_file(request, filename):
    # Specify the folder where your CSV files are located
    folder_path = Path("/home/tsp/Downloads/sanfil/file-upload/productionRemark")
    
    # Create the full file path
    file_path = folder_path / filename
    
    # Check if the file exists, otherwise raise a 404
    if file_path.exists() and file_path.suffix == '.csv':
        # Serve the file as a download
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
        return response
    else:
        raise Http404("File not found")
    

def deletion(request):
    dele()
    return render(request, 'app/dele.html')