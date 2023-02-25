from django.urls import path
from rest_framework_simplejwt import views
from .views import UsersView, UsersLoginView, UsersDetailView


urlpatterns = [
    path('users/', UsersView.as_view()),
    path('users/login/', UsersLoginView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
    path('users/<int:user_id>/', UsersDetailView.as_view()),
]