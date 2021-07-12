from django.shortcuts import render, redirect
from django.contrib.messages import error
from .models import Show

# Create your views here.

def index(request):
    return redirect('/shows')

def shows(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'index.html', context)

def show(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'show.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        errors = Show.objects.validate(request.POST)
        if errors:
            for e in errors:
                error(request, e)
            return redirect('/shows/new')
        show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
    return redirect('/shows')

def edit(request, id):
    show = Show.objects.get(id=id)
    context = {
        "show": show
    }
    return render(request, 'edit.html', context)

def update(request, id):
    if request.method == 'POST':
        errors = Show.objects.validate_edit(request.POST, id)
        if errors:
            for e in errors:
                error(request, e)
            return redirect(f'/shows/{id}/edit')
        show = Show.objects.get(id=id)
        show.title=request.POST['title']
        show.network=request.POST['network']
        show.release_date=request.POST['release_date']
        show.description=request.POST['description']
        show.save()
    return redirect(f'/shows/{id}')