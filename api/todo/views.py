from django.shortcuts import render


def submit_form(request):
    msg = None
    if request.method == 'POST':
        username = request.POST['username']
        address = request.POST['address']
        # .....
        msg = '提交成功'
    return render(request, 'form.html', locals())


def index(request):
    my_dict = {
        'key': 'hi',
    }
    my_list = ['wwc']
    return render(request, 'index.html', locals())
