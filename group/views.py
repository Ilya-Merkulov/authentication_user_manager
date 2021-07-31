
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import Groups
from .serializers import GroupsSerializer, CreateGroupsSerializer


# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def group_list(request):
    if request.method == 'GET':
        groups = Groups.objects.all()
        groups_serializer = GroupsSerializer(groups, many=True)
        return JsonResponse(groups_serializer.data, safe=False)

    elif request.method == 'POST':
        groups_data = JSONParser().parse(request)
        groups_serializer = GroupsSerializer(data=groups_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse(groups_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(groups_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
         group = Groups.objects.all().delete()
         group.delete()
         return JsonResponse({'message': '{} Groups were deleted successfully!'.format(group[0])}, 
         status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def group_detail(request, pk):
    try:
        group = Groups.objects.get(pk=pk)
    except Groups.DoesNotExist:
        return JsonResponse({"message": "The group does not exist "}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        groups_serializer = GroupsSerializer(group)
        return JsonResponse(groups_serializer.data, safe=False)
        # 'safe=False' for objects serializationd

    elif request.method == 'PUT':
        group_data = JSONParser().parse(request)
        groups_serializer = GroupsSerializer(group, data=group_data)
        if groups_serializer.is_valid():
            groups_serializer.save()
            return JsonResponse(groups_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(groups_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        group.delete()
        return JsonResponse({'message': 'Category were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)