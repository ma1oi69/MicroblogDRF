from rest_framework import serializers
from microblog.models.user import CustomUser
from django.contrib.auth.hashers import make_password
CHOICES_SEX = [('M', 'Men'), ('W', 'Women')]


class RegisterSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=100)
    sex = serializers.ChoiceField(choices=CHOICES_SEX)
    country = serializers.CharField()
    age = serializers.IntegerField(min_value=0, max_value=100)
    date_of_birthday = serializers.DateTimeField()
    about = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)

    def save(self):
        validated_data = self.validated_data

        user = CustomUser.objects.create(
            password=make_password(validated_data['password']),
            username=validated_data['username'],
            email=validated_data['email'],
            sex=validated_data['sex'],
            country=validated_data['country'],
            age=validated_data['age'],
            date_of_birthday=validated_data['date_of_birthday'],
            about=validated_data['about'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.save()
        return user