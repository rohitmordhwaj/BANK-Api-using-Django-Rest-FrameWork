from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import bank_info

@admin.register(bank_info)
class bank_infoAdmin(ImportExportModelAdmin):
    pass