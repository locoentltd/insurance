from django.urls import path

from portal.views import insured

urlpatterns = [
	path('list/', insured.InsuredList.as_view(), name='insured-list'),
	path('add/', insured.InsuredCreate.as_view(), name='insured-create'),
	path('<pk>/update', insured.InsuredUpdate.as_view(), name='insured-update'),
]
