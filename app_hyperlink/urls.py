
from django.conf.urls import url,include
from rest_framework import routers,views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
]
