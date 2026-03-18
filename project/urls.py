from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'landing.html')

urlpatterns = [
    path('', home),  # 👈 homepage
    path('admin/', admin.site.urls),
    path('api/news/', include('news.urls')),
]