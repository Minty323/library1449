from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DeleteView, UpdateView, DeleteView

def storage_home(request):
    cod = Articles.objects.order_by('-vrem')
    return render(request, 'storage/storage_home.html',{'cod': cod})

     
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('storage_home')
        else:
            error = 'Неверно заполнeно'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'storage/create.html', data)
