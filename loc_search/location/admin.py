from django.contrib import admin
from .models import City
from import_export.admin import ImportExportModelAdmin

class CityAdmin(ImportExportModelAdmin):
    list_display = ['admin_name1', 'admin_name2', 'admin_name3']
    list_per_page = 50
    list_filter = ['admin_name1']

admin.site.register(City, CityAdmin)
