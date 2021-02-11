from django.urls import path

from portal.views import user

urlpatterns = [
	path('password_change/',user.PasswordChange.as_view(),name='password_change'),
	path('user_change/',user.ProfileUpdate.as_view(),name='user_change'),
]


