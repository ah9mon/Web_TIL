from django.shortcuts import render

# Create your views here.
def orderpage(request):
    return render(request, 'orderpage.html')