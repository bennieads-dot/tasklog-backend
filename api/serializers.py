from rest_framework import serializers
from api.models import Priority, Group, Task


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ['id', 'priority']


class TaskSerializer(serializers.ModelSerializer):

    priority = serializers.SlugRelatedField(
        queryset=Priority.objects.all(),
        # read_only=True,
        allow_null=True,
        required=False,
        slug_field='priority'
    )

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'group', 'priority']


class GroupSerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Group
        fields = ['id', 'name', 'tasks']
