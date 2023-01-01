from django.urls import path
from . import views
urlpatterns = [
    path('addentry',views.addentry),
    path('claim',views.claim),
    path('addlink',views.getproduct),
    path('',views.index),
    
]