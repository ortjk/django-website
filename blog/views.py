from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostCreationForm, SendEmailForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    context = {
        "thomas_info": User.objects.get(username="thomasporter"),
    }

    if len(Post.objects.all()) >=5:
        # two steps necessary because django does not allow negative indexing
        blog_posts = Post.objects.all()[::-1]
        context["blog_posts"] = blog_posts[:5]
    else:
        context["blog_posts"] = Post.objects.all()[::-1]

    return render(request, "blog/home.html", context)


def blog_home(request):
    post_pages = Paginator(Post.objects.all()[::-1], 5)
    page_number = request.GET.get('page')

    context = {
        "blog_posts": post_pages.get_page(page_number),
    }   
        
    return render(request, "blog/blog.html", context)

def view_blog_post(request, post_id):
    context = {
        "post": Post.objects.get(id=post_id),
    }
    return render(request, "blog/view_post.html", context)

def contact(request):
    if request.method == "POST":
        email_form = SendEmailForm(request.POST)

        if email_form.is_valid():
            msg = f"{request.POST['first_name']} {request.POST['last_name']}, {request.POST['job_title']} at {request.POST['employer']} with email {request.POST['email']} sent the following message:\n\n{request.POST['content']}"

            send_mail(subject=request.POST['subject'],
            message=msg,
            from_email=request.POST['email'],
            recipient_list=["tgporter07@gmail.com"],
            fail_silently=False)

            messages.success(request, f"Email successfully sent!")
            return redirect("contact")

    else:
        email_form = SendEmailForm(initial={"employer": "[NONE]", "job_title": "[NONE]"})

    context = {
        "email_form": email_form,
    }

    return render(request, "blog/contact.html", context)

@login_required
def create_post(request):
    if request.method == "POST":
        p_form = PostCreationForm(request.POST, request.FILES)

        if p_form.is_valid():
            p_form.save()
            return redirect("/blog")

    else:
        p_form = PostCreationForm()

    context = {
        "post_form": p_form,
    }

    return render(request, "blog/create_post.html", context)
