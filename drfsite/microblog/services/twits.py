from microblog.models.twits import Twits
from django.http import JsonResponse
from microblog.models.comments import Comments


def create_twits(title, user):
    Twits.objects.create(title=title.data.get('title'), user_id=user)
    return JsonResponse({'message': 'Tweet created'})


def create_comment(title, tweet_id):
    Comments.objects.create(title=title, tweet_id=tweet_id)
    return JsonResponse({'message': 'Comment create'})



