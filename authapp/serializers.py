from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import timedelta

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all(), lookup="iexact")],
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), lookup="iexact")],
    )
    password = serializers.CharField(write_only=True, min_length=0, trim_whitespace=False)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        read_only_fields = ["id"]

    def validate_username(self, v):
        v = v.strip()
        if not v:
            raise serializers.ValidationError("Username cannot be blank.")
        return v

    def validate_email(self, v):
        return v.strip().lower()

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

UserModel = get_user_model()

class AuthLoginSerializer(TokenObtainPairSerializer):
    """
    Accepts either username or email in the `username` field.
    Example body: {"username": "alice" | "alice@example.com", "password": "..."}
    """
    def validate(self, attrs):
        username_or_email = attrs.get(self.username_field)
        if username_or_email and "@" in username_or_email:
            try:
                user = UserModel.objects.get(email__iexact=username_or_email)
                attrs[self.username_field] = user.get_username()
            except UserModel.DoesNotExist:
                pass

        data = super().validate(attrs)
        
        refresh = self.get_token(self.user)
        refresh.set_exp(lifetime=timedelta(days=30))
        access = refresh.access_token
        access.set_exp(lifetime=timedelta(hours=12))

        data["refresh"] = str(refresh)
        data["access"]  = str(access)

        return super().validate(attrs)
