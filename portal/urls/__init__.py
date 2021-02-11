from django.conf import settings
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView

from portal.views import (dashboard, quickquote, state,)

from portal.views.agent import AgentListAPI

from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'agents', AgentListAPI)

urlpatterns = [
	path('', RedirectView.as_view(url=reverse_lazy('dashboard'))),
	path('api/', include(router.urls)),
	path('api/states/', state.StateList.as_view(), name='api-state-list'),
	path('api/agents/', AgentListAPI.as_view()),
	path('api-auth/', include('rest_framework.urls')),
	path('agency/', include('portal.urls.agency')),
	path('agent/', include('portal.urls.agent')),
	path('insured/', include('portal.urls.insured')),
	path('quick/', include('portal.urls.quickquote')),
#	urlpatterns = format_suffix_patterns(urlpatterns)
#	url(r'^dashboard/', include('portal.urls.dashboard')),
	path('dashboard/', dashboard.index, name='dashboard'),
	path('user/', include('portal.urls.user')),
]

if 0 and settings.DEBUG:
	urlpatterns.append(path('tests/', include('portal.urls.tests')))

