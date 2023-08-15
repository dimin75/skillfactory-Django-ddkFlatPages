from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    return render(request, 'home.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html', {'flatpage': {'content': 'Sample content'}})

def page3(request):
    return render(request, 'page3.html')

@staff_member_required
def admin_page(request):
    return render(request, 'admin_page.html')

# Create your views here.
