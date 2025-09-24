from django.urls import path
from django.views.generic import TemplateView
from .views import AuthRegisterView, AuthLoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register", TemplateView.as_view(template_name="register.html"), name="auth-register-page"),
    path("login",    TemplateView.as_view(template_name="login.html"),    name="auth-login-page"),

    path("api/register", AuthRegisterView.as_view(), name="auth-register"),
    path("api/login",    AuthLoginView.as_view(),    name="auth-login"),
    path("refresh",  TokenRefreshView.as_view(), name="auth-refresh"),
]
