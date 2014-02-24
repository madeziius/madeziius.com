from django.conf.urls import patterns, url
#from blog.views import post


urlpatterns = patterns('blog.views',
    # Examples:
    #url(r'^$', 'blog.views.home', name='home'),
    url(r'^$', 'home', name='blog_home'),
    url(r'^contact/$', 'contact', name='blog_contact'),
    url(r'^about/$', 'about', name='blog_about'),
    #url(r'^newPost/$','newPost',name='blog_newPost'),
    #url(r'^blog/post/(?P<post_id>\d+)$', post, name='blog_post'),
    url(r'^bryllupsgave/$', 'bryllupsgave', name='blog_bryllupsgave'),
)
