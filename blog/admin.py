from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['author', 'title', 'anons', 'text', 'image']
        }),
        ('Categories and Tags', {
            'fields': ['category', 'tag']
        })
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
