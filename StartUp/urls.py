

from django.conf.urls import url,include
from rest_framework import routers
from StartUp.views import UserViewSet
from StartUp import views
from django.views.generic import TemplateView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^login', views.login),
    url(r'^home/', views.go_to_home),
    url(r'^data/', views.get_data),
    url(r'^user/', views.go_to_userlist),
    url(r'^$', views.login),
    url(r'^haha/$', TemplateView.as_view(template_name='error.html')),
]