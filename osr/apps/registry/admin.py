from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Coach, Sportsman, Parent, UMO, Rank, Sport_type, Survey, Primary)
class ViewAdmin(ImportExportModelAdmin):
    pass

