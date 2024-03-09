from django.urls import path

from .views import GetUsersView, GetUserProfileView, UpdateUserProfileView

urlpatterns = [
    path('get_users/', GetUsersView.as_view(), name='get_users'),
    path('get_user_profile/', GetUserProfileView.as_view(), name='get_user_profile'),
    path('update_user_profile/', UpdateUserProfileView.as_view(), name='update_user_profile'),
]