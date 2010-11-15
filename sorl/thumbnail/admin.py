from models import Preset
from django.contrib import admin

"""
   @todo - improve usability by adding custom form with fields, help, validation 
           for specifying geometry and options.
"""
class PresetAdmin(admin.ModelAdmin):
    list_display = ('name','geometry','options')
    list_editable = ('geometry')
admin.site.register(Preset, PresetAdmin)
