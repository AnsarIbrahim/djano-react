from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User

from .models import UserProfile
from .serializers import UserProfileSerializer, UserSerializer

class GetUsersView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        users = User.objects.all()

        users = UserSerializer(users, many=True)
        return Response(users.data)

class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            if user.is_authenticated:
                username = user.username

                user_profile = UserProfile.objects.get(user=user)
                user_profile = UserProfileSerializer(user_profile)

                return Response({'profile': user_profile.data, 'username': str(username)})
            else:
                return Response({'error': 'User is not authenticated'})
        except UserProfile.DoesNotExist:
            return Response({'error': 'User profile does not exist'})
        
class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
            try:
                user = self.request.user
                if user.is_authenticated:
                    username = user.username

                    data = self.request.data
                    first_name = data['first_name']
                    last_name = data['last_name']
                    phone = data['phone']
                    city = data['city']


                    UserProfile.objects.filter(user=user).update(first_name=first_name, last_name=last_name, phone=phone, city=city)

                    user_profile = UserProfile.objects.get(user=user)
                    user_profile = UserProfileSerializer(user_profile)

                    return Response({'profile': user_profile.data, 'username': str(username)})
                else:
                    return Response({'error': 'User is not authenticated'})
            except UserProfile.DoesNotExist:
                return Response({'error': 'User profile does not exist'})
            