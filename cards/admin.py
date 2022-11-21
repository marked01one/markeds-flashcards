from django.contrib import admin
from .models import Card, Group

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'box', 'group_name', 'date_created')
    
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Card, CardAdmin)
admin.site.register(Group, GroupAdmin)