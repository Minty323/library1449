from django.shortcuts import render
def index(request):
    data = {
    'title':'Главная страница'
    
    }
    return render(request, 'main/index.html', data)
def about(request):
    return render(request, 'main/about.html')
def info(request):
    return render(request, 'main/info.html')



