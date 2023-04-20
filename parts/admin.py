from django.contrib import admin
from .models import Part, ExcelSheet 

class PartAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', )
    ordering = ('title',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()




admin.site.register(Part, PartAdmin)


class ExcelAdmin(admin.ModelAdmin):
    list_display = ('upload_date','pk')
    search_fields = ('upload_date',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()




admin.site.register(ExcelSheet, ExcelAdmin)

