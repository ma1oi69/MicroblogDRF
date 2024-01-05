from rest_framework import serializers
CHOICES_SEX = [('M', 'Men'), ('W', 'Women')]


class UserSerializer(serializers.Serializer):
    sex = serializers.ChoiceField(choices=CHOICES_SEX)
    country = serializers.CharField()
    age = serializers.IntegerField()
    date_of_birthday = serializers.DateTimeField()
    about = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    