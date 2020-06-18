
from django.urls import path
from . import views

urlpatterns = [
  path('rater',views.RaterView),
  path('movieadd',views.MoviesAdd),
]







# from django.urls import path
# from . import views
# urlpatterns=[
#     path('',views.Login.as_view()),
#     path('register/',views.Register.as_view()),
# ]