from __future__ import print_function
from django.shortcuts import render,render_to_response,redirect
from django.template.context import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json
#from StartUp.forms.UserForm import User
from django.contrib.auth.models import User
from rest_framework import viewsets,serializers
from StartUp.serializers import UserSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
# Create your views here.


def login(request):
    return render_to_response('index.html',context_instance=RequestContext(request))

#@login_required
def go_to_home(request):
    #if request.method  == "POST":
        #return redirect('/user/')
    return render_to_response('home.html',context_instance=RequestContext(request))

def get_data(request):
    return HttpResponse(json.dumps("ok"));

def go_to_userlist(request):
    return render_to_response('user_list.html', context_instance=RequestContext(request))

def go_to_error(request):
    return render_to_response('error.html', context_instance=RequestContext(request))

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route()
    def check_detail(self, request, pk=None):

        return Response("ok")

    @list_route()
    def check_list(self, request):
        #self.paginate_queryset()
        return Response("list")

