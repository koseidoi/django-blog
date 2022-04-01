from django.urls import URLPattern, path 
from accounts import views

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='account_login'),
    path('logout/',views.LogoutView.as_view(),name='account_logout'),
    path('signup/',views.SignupView.as_view(),name='account_signup'),
]