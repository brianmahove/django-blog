from django.contrib import admin
from .models import Post, Category, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date', 'status']
    list_filter = ['status', 'created_date', 'publish_date', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_date'
    ordering = ['status', '-publish_date']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_date', 'approved']
    list_filter = ['approved', 'created_date']
    search_fields = ['author__username', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']