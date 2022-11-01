from rest_framework import serializers
from .models import FileUploading, FileInfo


class FileSerializer(serializers.ModelSerializer):
    """
    Сериализатор, который позволяет загрузить файл
    """
    class Meta:
        model = FileUploading
        fields = '__all__'


class FileInfoSerializer(serializers.ModelSerializer):
    """
    Сериализатор, который загружает инофрмацию из файла
    """
    class Meta:
        model = FileInfo
        fields = '__all__'
