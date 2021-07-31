from rest_framework import serializers
from .models import Groups


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = (
            'id',
            'GroupName',
            'GroupDescription')


class CreateGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('id','GroupName','GroupDescription')
     
    def create(self, validated_data):
        group = Groups(
            GroupName=validated_data['GroupName'],
            GroupDescription=validated_data['GroupDescription']
        )
        group.save()    
        return group
            
            