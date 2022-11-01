from django.contrib import admin
from .models import FileInfo, FileUploading


@admin.register(FileInfo)
class FileInfoAdmin(admin.ModelAdmin):
    fields = ['transaction_id', 'date_input', 'date_post', ]
    list_filter = ['date_input', 'date_post']


@admin.register(FileUploading)
class FileUploadingAdmin(admin.ModelAdmin):
    fields = ['csv_file']
