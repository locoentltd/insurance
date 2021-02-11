from django.urls import path

from portal.views import agency

urlpatterns = [
	path('list/', agency.AgencyList.as_view(), name='agency-list'),
	path('add/', agency.AgencyCreate.as_view(), name='agency-create'),
	path('<pk>/update', agency.AgencyUpdate.as_view(), name='agency-update'),
]
