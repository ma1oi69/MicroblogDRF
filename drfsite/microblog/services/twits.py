from microblog.models.twits import Twits
from django.http import JsonResponse
from microblog.models.user import CustomUser
from django.contrib.auth.hashers import make_password
from microblog.models.comments import Comments


def create_twits(title, user):
    tweet = Twits.objects.create(title=title.data.get('title'), user_id=user)
    return JsonResponse({'message': 'Tweet created'})


def create_user(email, password, username):
    password = make_password(password)
    user = CustomUser.objects.create(email=email, password=password, username=username)
    return JsonResponse({'message': 'User created'})


def create_comment(title, tweet_id):
    comment = Comments.objects.create(title=title, tweet_id=tweet_id)
    return JsonResponse({'message': 'Comment create'})


