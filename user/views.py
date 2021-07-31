from django.shortcuts import render
from rest_framework import generics


from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import RegisterUserSerializer, UsersSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny

from .models import User

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == "DELETE":
        users = User.objects.all().delete()
        users.delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(users[0])}, 
        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({"message": "The User does not exist "}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = UsersSerializer(user)
        return JsonResponse(user_serializer.data, safe=False)
        # 'safe=False' for objects serializationd

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return JsonResponse({'message': 'User were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class UserListView(generics.ListCreateAPIView):
    """Handles creating and listing Users."""
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
