from django.urls import path
from . import views


urlpatterns = [
    path('',  views.main, name = "homepage"),
    path('displayresults/', views.displayresults, name = "displayresults"),
]