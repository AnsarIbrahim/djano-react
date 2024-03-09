from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('authentication.urls')),
    path('user/', include('user_profile.urls')),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]