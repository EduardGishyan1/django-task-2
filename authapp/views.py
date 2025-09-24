from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegisterSerializer, AuthLoginSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class AuthRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        s = UserRegisterSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        user = s.save()
        return Response({"user": UserRegisterSerializer(user).data}, status=status.HTTP_201_CREATED)

class AuthLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = AuthLoginSerializer

class RegisterPageView(TemplateView):
    template_name = "register.html"

class LoginPageView(TemplateView):
    template_name = "login.html"  