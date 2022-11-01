from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, ListAPIView
import csv
from drf_yasg.utils import swagger_auto_schema
from rest_framework.settings import api_settings
from .models import FileUploading
from .serializers import FileSerializer, FileInfoSerializer
from .models import FileInfo
from .filters import FileInfoFilter
from rest_framework_csv import renderers


class FileAPIView(ListCreateAPIView):
    """
    API для загрузки файла
    """
    queryset = FileUploading.objects.all()
    serializer_class = FileSerializer

    @swagger_auto_schema(
        operation_summary="List all files",
        operation_description="This endpoint shows all files"
    )
    def get(self, request, *args, **kwargs):
        return self.list(request)

    @swagger_auto_schema(
        operation_summary="Post files",
        operation_description="This endpoint loads all information into the database"
    )
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            file_path = file_serializer.data['csv_file'][1:]
            file = open(file_path, encoding='utf-8').readlines()[1:]
            csv_reader = csv.reader(file)
            for row in csv_reader:
                transaction_id = row[0]
                request_id = row[1]
                terminal_id = row[2]
                partner_object_id = row[3]
                amount_total = row[4]
                amount_original = row[5]
                commission_ps = row[6]
                commission_client = row[7]
                commission_provider = row[8]
                date_input = row[9]
                date_post = row[10]
                status = row[11]
                payment_type = row[12]
                payment_number = row[13]
                service_id = row[14]
                service = row[15]
                payee_id = row[16]
                payee_name = row[17]
                payee_bank_mfo = row[18]
                payee_bank_account = row[19]
                payment_narrative = row[20]
                FileInfo.objects.create(
                    transaction_id=transaction_id,
                    request_id=request_id,
                    terminal_id=terminal_id,
                    partner_object_id=partner_object_id,
                    amount_total=amount_total,
                    amount_original=amount_original,
                    commission_ps=commission_ps,
                    commission_client=commission_client,
                    commission_provider=commission_provider,
                    date_input=date_input,
                    date_post=date_post,
                    status=status,
                    payment_type=payment_type,
                    payment_number=payment_number,
                    service_id=service_id,
                    service=service,
                    payee_id=payee_id,
                    payee_name=payee_name,
                    payee_bank_mfo=payee_bank_mfo,
                    payee_bank_account=payee_bank_account,
                    payment_narrative=payment_narrative
                )
            return redirect('file-api')


class FileInfoAPI(ListAPIView):
    """
    API для вывода информации из загруженных файлов
    """
    queryset = FileInfo.objects.all()
    serializer_class = FileInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FileInfoFilter

    @swagger_auto_schema(
        operation_summary="File info",
        operation_description="This endpoint shows all files info"
    )
    def get(self, request, *args, **kwargs):
        return self.list(request)


class FileInfoCsv(ListAPIView):
    """
    API для загрузки информации из файла в формате csv
    """
    queryset = FileInfo.objects.all()
    serializer_class = FileInfoSerializer
    renderer_classes = (renderers.CSVRenderer, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
