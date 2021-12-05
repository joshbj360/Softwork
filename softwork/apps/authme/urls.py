from django.urls import path, include

from dj_rest_auth.views import PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView

urlpatterns = [
    path('users/', include('dj_rest_auth.urls')),
    
    path(
        'users/registration/account-confirm-email/<str:key>/',
         ConfirmEmailView.as_view(), name='account_confirm_email'),
    
    path('users/registration/', include('dj_rest_auth.registration.urls')),
    
    # Email Verification urls
    path(
        'users/account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    
    path(
        'users/password/reset/confirm/<slug:uidb64>/<slug:token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    
]
