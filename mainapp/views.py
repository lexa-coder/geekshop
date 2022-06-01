from django.shortcuts import render


# Create your views here.
def index(request):
    cotext = {
        'user_list': [
            {
                'first_name': 'alexey',
                'last_name': 'papshev',
                'age': 30

            },
            {
                'first_name': 'oleg',
                'last_name': 'maslov',
                'age': 31

            }
        ]
    }
    return render(request, 'mainapp/index.html', cotext)


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')
