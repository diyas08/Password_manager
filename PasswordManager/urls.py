from django.urls import path
from .views import index, PasswordLevel1, PasswordLevel2, PasswordLevel3

urlpatterns = [
    path('index/', index),
    path('password1/', PasswordLevel1.as_view()),
    path('password2/', PasswordLevel2.as_view()),
    path('password3/', PasswordLevel3.as_view())
]
