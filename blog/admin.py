from django.contrib import admin

__author__ = 'mad'

from blog.models import BlogPosts,Comments,Gave

class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 3

class BlogPostsAdmin(admin.ModelAdmin):
    model = BlogPosts
    inlines = [CommentsInline]

class GaveAdmin(admin.ModelAdmin):
	model = Gave

admin.site.register(BlogPosts, BlogPostsAdmin)
admin.site.register(Gave)
