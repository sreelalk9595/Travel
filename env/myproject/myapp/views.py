from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def tour(request):
    return render(request,'tour.html')
def package(request):
    return render(request,'package.html')

