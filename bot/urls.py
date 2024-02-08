from django.urls import path
from .views import HomeView,Demo

urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('h/',Demo.as_view())
]