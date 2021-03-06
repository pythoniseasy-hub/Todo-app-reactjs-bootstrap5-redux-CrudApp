from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import *

urlpatterns = [
    path('test',test),
    path('', ApiRoot.as_view(), name='root'),
    path('todos', ToDoAppViews.as_view(), name="todos"),

    path('register', UserView.as_view(), name="register"),
    path('verify/<auth_token>', VerifyAccount, name="VerifyAccount"),

    path('loginCredentials', loginCredentialsView.as_view(), name='loginCredentials'),
    path('login', TokenObtainPairView.as_view(), name='login'),

    path('getUser', getUserView.as_view(), name="getUser"),
    path('deleteUser', deleteUserView.as_view(), name="deleteUser"),
    path('updateUser', updateUserView.as_view(), name="updateUser"),

    path('socialSignin', socialSigninView.as_view(), name="socialSignin"),

    path('change_password', changePasswordView.as_view(), name='change_password'),

    path('forgot_password_email_verification', forgot_password_email_verification_View.as_view(
    ), name='forgot_password_email_verification'),

    path('forgot_password_otp_verification', forgot_password_otp_verification_View.as_view(
    ), name='forgot_password_otp_verification'),

    path('forgot_password_with_new_password', forgot_password_with_new_password_View.as_view(
    ), name='forgot_password_with_new_password'),
]
