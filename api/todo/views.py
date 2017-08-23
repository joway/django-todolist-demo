from django.shortcuts import render


def index(request):
    user = request.user
    my_dict = {
        'key': 'good',
    }
    my_list = ['bad']
    return render(request, 'index.html', locals())
