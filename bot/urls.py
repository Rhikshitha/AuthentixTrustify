from django.urls import path
from .views import HomeView,Demo,SendMessage

urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('h/',Demo.as_view()),
    path('send_message/', SendMessage.as_view(), name="send_message"),
]