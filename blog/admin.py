from django.contrib import admin

__author__ = 'mad'

from blog.models import BlogPosts,Comments

class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 3

class BlogPostsAdmin(admin.ModelAdmin):
    model = BlogPosts
    inlines = [CommentsInline]


admin.site.register(BlogPosts, BlogPostsAdmin)