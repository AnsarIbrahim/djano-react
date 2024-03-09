from django.urls import path
from .views import GetCSRFTOKEN, SignupView, LoginView, CheckAuthenticated, LogoutView, DeleteAccountView

urlpatterns = [
    path('get_csrf', GetCSRFTOKEN.as_view(), name='get_csrf'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('authenticated', CheckAuthenticated.as_view(), name='authenticated'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('delete', DeleteAccountView.as_view(), name='delete'),
]