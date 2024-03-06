from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import auth
from rest_framework import permissions
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator

from user_profile.models import UserProfile
from .serializers import UserSerializer


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFTOKEN(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'success': 'CSRF cookie set'})


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        password = data['password']
        repassword = data['repassword']

        try:
            if password == repassword:
                if User.objects.filter(username=username).exists():
                    return Response({'error': 'Username already exists'})
                else:
                    if len(password) < 6:
                        return Response({'error': 'Password must be at least 6 characters'})
                    else:
                        user = User.objects.create_user(username=username, password=password)
                     
                        user = User.objects.get(username=username)

                        UserProfile.objects.create(user_id=user.id, first_name='', last_name='', phone='', city='')
                       
                        return Response({'success': 'User created successfully'})
            else:
                return Response({'error': 'Password not matching'})
        except:
            return Response({'error': 'Something went wrong'})


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        password = data['password']

        try:
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return Response({'success': 'User logged in', 'username': username})
            else:
                return Response({'error': 'Invalid credentials'})
        except:
            return Response({'error': 'Something went wrong'})


class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success': 'User logged out'})
        except:
            return Response({'error': 'Something went wrong'})
        
class CheckAuthenticated(APIView):
    def get(self, request, format=None):
       user = self.request.user
       try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                    return Response({'isAuthenticated': True, 'session_id': request.session.session_key})
            else:
                    return Response({'isAuthenticated': False})
       except:
            return Response({'error': 'Something went wrong'})


class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user
        try:
            user = User.objects.filter(id=user.id).delete()
            return Response({'success': 'User deleted'})
        except:
            return Response({'error': 'Something went wrong'})
        

class GetUsersView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        users = User.objects.all()

        users = UserSerializer(users, many=True)
        return Response(users.data)