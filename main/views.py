from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495962',
        'name': 'Wildan Muhammad Hafidz',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)