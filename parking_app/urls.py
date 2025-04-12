from django.urls import path
from . import views

urlpatterns = [
  
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('process_login/', views.login_view, name='process_login'),  # This should exist
    path('process_signup/', views.signup_view, name='process_signup'),
    path('look_for_parking/', views.look_for_parking, name='handle_parking_request'),
    path('look_parking/', views.look_park, name='look_for_parking'),
    path('book_parking/', views.look_for_parking, name='book_parking'),
    path('about/', views.about, name='about'),
    path('mainpage/', views.home, name='home'),
]
