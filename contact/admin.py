from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'show')
    search_fields = ('id', 'first_name', 'last_name',)
    list_editable = ('first_name', 'last_name', 'show')
    list_display_links = ('id', 'phone',)
    ordering = ('id',) # ordenando em ordem crescente, '-id' para decrescente
    # list_filter = 'created_date', # Filtro (no caso para data de criação de contato)
    list_max_show_all = 200
    list_per_page = 10
    
@admin.register(models.Category)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',) # ordenando em ordem crescente, '-id' para decrescente