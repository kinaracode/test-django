from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Kinara Code',
        'kontributor' : '@kinarakode',
    }
    return render(request, 'about/index.html', context)