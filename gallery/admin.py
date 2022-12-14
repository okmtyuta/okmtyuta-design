from django.contrib import admin
from .models import *

@admin.register(IllustComment)
class IllustCommentAdmin(admin.ModelAdmin):
    actions = ["make_comments_private", "make_comments_public"]

    def make_comments_private(self, request, queryset):
        queryset.update(is_public=False)
    def make_comments_public(self, request, queryset):
        queryset.update(is_public=True)
    
    make_comments_private.short_description = "Make comments private"
    make_comments_public.short_description = "Make comments public"

admin.site.register(IllustTag)
admin.site.register(Illust)
# admin.site.register(IllustComment)