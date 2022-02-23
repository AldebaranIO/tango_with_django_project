from django.contrib import admin
from rango.models import Category, Page



class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category',"url")

#class PageAdmin must be in front of where calling it
admin.site.register(Category)
admin.site.register(Page,PageAdmin)