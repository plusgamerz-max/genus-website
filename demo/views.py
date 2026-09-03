from django.shortcuts import render

def textarea_demo(request):
    return render(request, 'textarea_demo.html')