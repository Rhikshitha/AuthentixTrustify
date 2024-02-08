from django.urls import path
from .views import RegisterView,LogInView,VerifyEmail

urlpatterns=[
    path('login/',LogInView.as_view(),name="login"),
    path('register/',RegisterView.as_view(),name="register"),
    path('verify_email/',VerifyEmail.as_view(),name="verify_email")
]