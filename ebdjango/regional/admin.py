from django.contrib import admin
from regional.models import *
from import_export.admin import ImportExportModelAdmin 
from import_export import resources

class ActaResource(resources.ModelResource):
    class Meta:
        model = Regional

class Regional_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('regional',)
    class Meta:
        model = Regional

admin.site.register(Regional, Regional_Admin)
