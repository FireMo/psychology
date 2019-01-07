from django.shortcuts import render

# Create your views here.


def psychology_test(request):
    return render(request, 'psych/psychtest.html')
