from django.contrib import admin
from .models import Board
# Register your models here.
@admin.register(Board)
class adminBoard(admin.ModelAdmin):
    list_display = ('author','title','file','createtime',)
    search_fields = ('author',)
