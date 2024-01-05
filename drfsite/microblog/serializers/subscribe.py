from microblog import serializers
from microblog.models.follower import Follower


# class FollowersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Follower
#         fields = '__all__'
#
#     def create(self, validated_data):
#         follower = CustomUser.objects.get(id=validated_data['followers'])
#         subscriptions = CustomUser.objects.get(id=validated_data['subscriptions'])
#
#         follower_instance = Follower.objects.create(
#             follower=follower,
#             subscriptions=subscriptions,
#         )
#
#         return follower_instance


