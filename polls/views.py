# Create your views here.

from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.decorators import protected_resource
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from polls.apps import query
from zcore.urls import UserSerializer


@protected_resource()
@api_view(["GET"])
def user_list(request):
    users = User.objects.all()
    data = [UserSerializer(user).data for user in users]
    return Response(data)


@protected_resource()
@api_view(["GET", "POST", "DELETE"])
def user_details(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@protected_resource(scopes=["groups"])
def group_list(request):
    groups = Group.objects.all()
    data = [UserSerializer(group).data for group in groups]
    return Response(data)


@protected_resource()
def users_raw(request):
    data = query("SELECT * FROM auth_user", "default")
    return JsonResponse(data, safe=False)


@protected_resource()
@csrf_exempt
def user_details_raw(request, pk):
    if request.method == "GET":
        data = query("SELECT * FROM auth_user WHERE id='{id}'".format(id=pk), "default")
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        data = query("UPDATE auth_user SET  username='{username}',email='{email}' WHERE id='{id}'".format(
            id=pk,
            username=request.POST.get('username'),
            email=request.POST.get('email')), "default")
        return JsonResponse(data, safe=False)
