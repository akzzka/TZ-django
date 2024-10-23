from django.shortcuts import render, redirect
from .forms import SongForm

def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')
    else:
        form = SongForm()

    return render(request, '')

