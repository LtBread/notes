from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField

from .models import Project, ToDo


class ProjectModelSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    user = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'
