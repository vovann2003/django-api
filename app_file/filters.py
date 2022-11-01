from django_filters import rest_framework as filters
from app_file.models import FileInfo


class FileInfoFilter(filters.FilterSet):
    """
    Класс фильтра по полям файла
    """
    transaction_id = filters.NumberFilter(field_name="transaction_id")
    terminal_id = filters.NumberFilter(field_name="terminal_id", lookup_expr="gte")
    status = filters.CharFilter(field_name="status")
    payment_type = filters.CharFilter(field_name="payment_type")
    date_post_from = filters.DateTimeFilter(field_name="date_post", lookup_expr="gte")
    date_post_to = filters.DateTimeFilter(field_name="date_post", lookup_expr="lte")
    payment_narrative = filters.CharFilter(field_name="payment_narrative", lookup_expr="icontains")

    class Meta:
        model = FileInfo
        fields = (
            'transaction_id',
            'terminal_id',
            'status',
            'payment_type',
            'date_post_from',
            'date_post_to',
            'payment_narrative',
        )
