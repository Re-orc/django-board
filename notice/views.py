from django.shortcuts import render,get_object_or_404,redirect
from .models import Board
from .forms import noticeForm,ResiterForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

def listview(request):
    posts = Board.objects.all().order_by('-createtime')
    search = request.GET.get('q','')
    if search:
        posts = posts.filter(title__icontains=search)

    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'listview.html',{'posts':posts,'search':search})

@login_required
def detailview(request,pk):
    posts = get_object_or_404(Board,pk=pk)
    return render(request,'detailview.html',{'posts':posts})

@login_required
def createview(request):
    if request.method == 'POST':
        form = noticeForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = noticeForm()
    return render(request,'createview.html',{'form':form})

@login_required
def updateview(request,pk):
    posts = get_object_or_404(Board,pk=pk)
    if request.method == 'POST':
        form = noticeForm(request.POST,request.FILES,instance=posts)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('notice:detail',pk=pk)
    else:
        form = noticeForm(instance=posts)
    return render(request,'updateview.html',{'form':form})

@login_required
def deleteview(request,pk):
    posts = get_object_or_404(Board,pk=pk)
    if request.method == 'POST':
        posts.delete()
        return redirect('/')
    return render(request,'deleteview.html',{'posts':posts})

def register(request):
    if request.method == 'POST':
        form = ResiterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request,'accounts/register_done.html',{'new_user':new_user})
    else:
        form = ResiterForm()
    return render(request,'accounts/register.html',{'form':form})
