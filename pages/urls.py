from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('category',views.category,name='category'),
    path('services',views.services,name='services'),
    path('details<int:id>', views.details, name='details'),
    
]
