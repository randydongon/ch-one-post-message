from django.contrib import admin
from messageapp.models import MessagePost
# Register your models here.


@admin.register(MessagePost)
class MessagePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'date_send')
    list_filter = ('created', 'status', 'author', 'date_send')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_heirarchy = ('-date_send')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', 'date_send')
