# Create your views here.
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context import RequestContext
from blog.forms import NewBlogPostForm
from blog.models import BlogPosts, Gave
from django.http import Http404, HttpResponse
from django.utils import simplejson

def home(request):
    blogs = BlogPosts.objects.order_by("date")[:5]
    return render_to_response('blog/home.html', { "blogs": blogs, 'show_comment': False}, context_instance=RequestContext(request))

#def post(request, post_id):
#    blog = get_object_or_404(BlogPosts, pk=post_id)
#    return render_to_response('blog/home.html', { "blogs": [blog], 'show_comment': True}, context_instance=RequestContext(request))

def contact(request):
    return render(request, 'blog/contact.html', locals())
def bryllupsgave(request):
    gave = Gave.objects.all()
    return render(request, 'blog/bryllupsgave.html', {'Gave':gave})
def bryllupsgavepost(request, gave_id):
    gave = get_object_or_404(Gave, pk=int(gave_id))
    gave.kjopt = not gave.kjopt
    gave.save()
    message = {}
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype="application/json")	
def about(request):
    return render (request, 'blog/about.html', locals())
def start(request):
    return render (request, 'blog/start.html', locals())

#def newPost(request):
#    form = NewBlogPostForm(request.POST or None)

#    if request.method == 'POST': # If the form has been submitted...
#        if form.is_valid(): # All validation rules pass
#            title = form.cleaned_data.get('title')
#
#    return render(request,'blog/newPost.html',{'form':form})
