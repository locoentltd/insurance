from django.urls import path

from portal.views import quickquote

urlpatterns = [
	path('',quickquote.QuickQuoteStateSelect.as_view(),name='quick-select-state'),
	path('state/<pk>/',quickquote.QuickQuoteCreate.as_view(),name='quick-create'),
	path('<pk>/update',quickquote.QuickQuoteUpdate.as_view(),name='quick-update'),
]
