from django.contrib import admin
from .models import Tag,TextSnippet

admin.site.site_header = "Messages Admin"
admin.site.site_title = "Messages"
admin.site.index_title = "Welcome to Messages Admin"


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag',)
    search_fields = ('id', 'tag', )

admin.site.register(Tag, TagAdmin)


class TextSnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('id', 'title', )

admin.site.register(TextSnippet, TextSnippetAdmin)