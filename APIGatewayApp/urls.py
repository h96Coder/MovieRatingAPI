
from django.urls import path
from .views import login,Register


urlpatterns = [
    path('login', login),
    path('register',Register),
]







# from django.urls import path
# from . import views
# urlpatterns=[
#     path('',views.Login.as_view()),
#     path('register/',views.Register.as_view()),
# ]