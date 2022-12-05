from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

    list_display = ("title", "is_public", "is_picked_up")
    def add_view(self, request, form_url='', extra_context=None):
        self.readonly_fields = ('created_at', "updated_at")
        return self.changeform_view(request, None, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.readonly_fields = ('created_at', "updated_at")
        return self.changeform_view(request, object_id, form_url, extra_context)


admin.site.register(Article, ArticleAdmin)
