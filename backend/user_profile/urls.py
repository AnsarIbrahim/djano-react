from django.urls import path, include

from .views import GetUserProfileView, UpdateUserProfileView

urlpatterns = [
    path('user', GetUserProfileView.as_view(), name='get_user_profile'),
    path('update', UpdateUserProfileView.as_view(), name='update_user_profile'),
]