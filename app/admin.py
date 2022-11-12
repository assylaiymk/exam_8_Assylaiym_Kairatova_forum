from django.contrib import admin

from app.models import Theme


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_filter = ('id', 'title', 'author', 'created_at')
    search_fields = ('title', 'author')
    fields = ('title', 'author', 'description', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Theme, ThemeAdmin)

