from django.contrib import admin

# Register your models here.
from . import models

class MovieAdmin(admin.ModelAdmin):
    #customizations formed for admin
    fields = ['release_year','title','length']    

    search_fields = ['title','length']

    list_filter = ['release_year', 'length',]

    list_display = ['title', 'length', 'release_year',]

    list_editable = ['length']

admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Customer)
