
from django.conf.urls import url,include
from rest_framework import routers
from app.views import UserViewSet,snippet_list,snippet_detail,SnippetList,SnippetDetail,SnipList,SnipDetail


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'snip', UserViewSet)
#router.register()
urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^snippets/$',snippet_list),
    url(r'^snippets2/$',SnippetList.as_view()),
    url(r'^snippets2/(?P<pk>[0-9]+)/$',SnippetDetail.as_view()),
    url(r'^s3/$',SnipList.as_view()),
    url(r'^s3/(?P<pk>[0-9]+)/$', SnipDetail.as_view()),
]

