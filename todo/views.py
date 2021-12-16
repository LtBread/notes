from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from .serializers import ProjectModelSerializer, ToDoModelSerializer
from .models import Project, ToDo


class ProjectPaginator(LimitOffsetPagination):
    default_limit = 10


class ToDoPaginator(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPaginator
    filterset_fields = ['name']


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoPaginator
    filterset_fields = ['project']

    def perform_destroy(self, instance):
        instance.is_completed = True
        instance.save()

# class ProjectViewSet(CreateModelMixin,
#                      ListModelMixin,
#                      RetrieveModelMixin,
#                      UpdateModelMixin,
#                      DestroyModelMixin,
#                      GenericViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = Project.objects.all()
#     serializer_class = ProjectModelSerializer
#     pagination_class = Paginator
#     filterset_fields = ['name']

# def get_queryset(self):
#     if 'name' in self.request.query_params:
#         return Project.objects.filter(name=self.request.query_params.get('name'))
#     return Project.objects.all()
