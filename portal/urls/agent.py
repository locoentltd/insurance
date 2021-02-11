from django.urls import path

from portal.views import agent

urlpatterns = [
	path('list/', agent.AgentList.as_view(), name='agent-list'),
	path('add/', agent.AgentCreate.as_view(), name='agent-create'),
	path('<pk>/update', agent.AgentUpdate.as_view(), name='agent-update'),
]
