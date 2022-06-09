from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer



class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required = True,
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )
    
    password = serializers.CharField(
        write_only = True,
        required=True,
        validators = [validate_password],
        style = {"input_type" : "password"}
    )
    
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style = {"input_type" : "password"}
    )
    
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password2"
        ]
        

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"message": "Password fields didn't match"}
            )
        return data

    def create(self, validated_data):
        password = validated_data.get("password")
        validated_data.pop("password2")
        print(validated_data)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserTokenSerizalizer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")


class CustomTokenSerializer(TokenSerializer):
    
    user = UserTokenSerizalizer(read_only=True)
    
    class Meta(TokenSerializer.Meta):
        fields = ("key", "user")