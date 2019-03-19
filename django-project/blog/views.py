from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Kinara Code',
        'kontributor':'@kinaracode',
    }
    return render(request,'blog/index.html', context)