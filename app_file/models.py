from django.db import models


class FileInfo(models.Model):
    """
    Модель для хранения информации с загруженного файла
    """

    ACCEPTED = 'ACC'
    DECLINED = 'DEC'
    CASH = 'CASH'
    CARD = 'CARD'
    REPLENISHMENT = 'REP'
    PUMB = 'PUMB'
    PRIVAT = 'PRIVAT'
    OSCHAD = 'OSCHAD'
    MONEY_TRANSFER = 'MT'

    STATUS_CHOICES = (
        (ACCEPTED, 'accepted'),
        (DECLINED, 'declined'),
    )

    PAYMENT_TYPE = (
        (CASH, 'cash'),
        (CARD, 'card'),
    )

    SERVICE = (
        (REPLENISHMENT, 'replenishment_of_the_card'),
    )

    PAYEE_NAME = (
        (PUMB, 'pumb'),
        (PRIVAT, 'privat'),
        (OSCHAD, 'oschad'),
    )

    PAYMENT_NARRATIVE = (
        (MONEY_TRANSFER, 'money_transfer'),
    )
    # id = models.IntegerField(auto_created=True, primary_key=True, verbose_name='id')
    transaction_id = models.IntegerField(verbose_name='transaction id')
    request_id = models.IntegerField(verbose_name='request id')
    terminal_id = models.IntegerField(verbose_name='terminal id')
    partner_object_id = models.IntegerField(verbose_name='partner object id')
    amount_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='amount total')
    amount_original = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='amount original')
    commission_ps = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='commission PS')
    commission_client = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='commission client')
    commission_provider = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='commission provider')
    date_input = models.DateTimeField(verbose_name='date input')
    date_post = models.DateTimeField(verbose_name='date post')
    status = models.CharField(choices=STATUS_CHOICES, default=ACCEPTED, max_length=20, verbose_name='status')
    payment_type = models.CharField(choices=PAYMENT_TYPE, default=CASH, max_length=20, verbose_name='payment type')
    payment_number = models.CharField(max_length=20, verbose_name='payment number')
    service_id = models.IntegerField(verbose_name='service id')
    service = models.CharField(choices=SERVICE, default=REPLENISHMENT, max_length=20, verbose_name='service')
    payee_id = models.IntegerField(verbose_name='payee id')
    payee_name = models.CharField(choices=PAYEE_NAME, default=PRIVAT, max_length=20, verbose_name='payee name')
    payee_bank_mfo = models.IntegerField(verbose_name='payee bank mfo')
    payee_bank_account = models.CharField(max_length=20, verbose_name='payee bank account')
    payment_narrative = models.CharField(choices=PAYMENT_NARRATIVE, default=MONEY_TRANSFER, max_length=200, verbose_name='payment narrative')

    class Meta:
        db_table = 'app_file_loading'
        verbose_name = 'file info'
        verbose_name_plural = 'file info`s'


class FileUploading(models.Model):
    """
    Модель для загрузки файла
    """
    csv_file = models.FileField(upload_to='files/%Y/%m/%d', verbose_name='csv file')

    class Meta:
        db_table = 'file_uploading'
        verbose_name_plural = 'file uploading'

