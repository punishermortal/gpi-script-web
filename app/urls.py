from django.urls import path
from .views import upload_file,upload_form,csv_file_list,download_csv_file,deletion

urlpatterns = [
    # path("select-files/", select_files, name="select_files"),
    path('upload/', upload_file, name='upload_file'),
    path('upload_form/', upload_form, name='upload_form'),
    path('download/', csv_file_list, name='download'),
    path('dele/', deletion, name='dele'),
    path('csv-files/download/<str:filename>/', download_csv_file, name='download-csv'),
]
