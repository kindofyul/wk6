from django.shortcuts import render, redirect, get_object_or_404
from .models import Community

def home(request):
    community = Community.objects.all()
    post_count = Community.objects.all().count()
    return render(request, "home.html", {'community':community, 'post_count':post_count})

def detail(request, id):
    community = get_object_or_404(Community, pk = id)
    return render(request, 'detail.html', {'community':community})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_community = Community()
    new_community.title = request.POST["title"]
    new_community.rate = request.POST['rate']
    # new_community.now = request.POST['now']
    new_community.review = request.POST['body']
    new_community.save()
    return redirect('detail', new_community.id)



