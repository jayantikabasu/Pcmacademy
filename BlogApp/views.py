from django.shortcuts import render,HttpResponse, redirect,get_object_or_404
from .models import *
from update.models import Nav1, AboutPage_Head
from django.contrib import messages  

# Create your views here.
def blog(request):

    try:
        Nav1Obj = Nav1.objects.latest('created_at')
    except Nav1.DoesNotExist:
        Nav1Obj = None
    try:
        HeadObj = AboutPage_Head.objects.latest('created_at')
    except AboutPage_Head.DoesNotExist:
        HeadObj = None
    try:
        BlogObj = BlogPage_blog.objects.all()
    except BlogPage_blog.DoesNotExist:
        BlogObj = None
    

    context = { 'Nav1Obj' : Nav1Obj,
               'HeadObj' : HeadObj,
               'BlogObj' : BlogObj,
    }

    return render(request, 'blog.html',context)

def show_blog(request,slug):

    try:
        Nav1Obj = Nav1.objects.latest('created_at')
    except Nav1.DoesNotExist:
        Nav1Obj = None
    try:
        HeadObj = AboutPage_Head.objects.latest('created_at')
    except AboutPage_Head.DoesNotExist:
        HeadObj = None
    try:
        ShowblogObj = BlogPage_blog.objects.get(slug=slug) 
    except BlogPage_blog.DoesNotExist:
        ShowblogObj = None


    context = {'Nav1Obj' : Nav1Obj,
               'HeadObj' : HeadObj,
               'ShowblogObj':ShowblogObj
               }
    
    try:
        if request.method == "POST":
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            phone = request.POST.get("phone", "")
            comment = request.POST.get("comment", "")

            if not phone:
                phone = None

            blog_post = get_object_or_404(BlogPage_blog, slug=slug)


            if(
                len(name) < 3 
                or len(email) < 12 
                or len(comment) < 15
            ):
                raise ValueError("Invalid imput. Please check your details and try again.")
            
            else:
                CommentFormObj = BlogComment(
                    name = name,
                    phone = phone,
                    email = email,
                    comment = comment,
                    relation = blog_post,

                )
                CommentFormObj.save()
                return redirect("blog")
    
    except Exception:
        return redirect("blog")

    
    return render(request, 'showblog.html',context)

