from django.shortcuts import render


def index(request):
    context = {
        'judul' : ' Welcome Kinara Code',
        'kontributor' : '@kinaracode',
    }

    return render(request,'index.html',context)