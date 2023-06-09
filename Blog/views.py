from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from .forms import BlogForm,ProductForm
def list(request):
    list=Blog.objects.all()
    context={'list':list}
    return render(request,'list.html',context)

def blog(request,id):
    blog =get_object_or_404(Blog,id=id)
    context={'blog':blog}
    return render (request,'blog.html',context)

def blog_create(request):
    form=BlogForm()

    if request.method == 'POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

    context={'form':form}
    return render(request,'blog_create.html',context)

def product_create(request):
    form=ProductForm(request.POST)
    context={
        'form':form
    }
    return render(request,'imtahanim_var.html ',context)

# Create your views here.
