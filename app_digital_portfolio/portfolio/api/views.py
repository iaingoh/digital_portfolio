from portfolio.models import Project, ProjectSubtitle, BulletPoint
from portfolio.api.serializers import (
    ProjectDetailSerializer,
    ProjectSerializer,
)
from rest_framework.generics import ListAPIView, RetrieveAPIView
# from rest_framework import routers, serializers, viewsets

# class ProjectSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Project
#         fields = '__all__'

# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# class ProjectSubtitleSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ProjectSubtitle
#         fields = '__all__'

# class ProjectSubtitleViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.filter(project_id=SOMETHING_GOES_HERE)
#     serializer_class = ProjectSerializer

# router = routers.SimpleRouter()
# router.register(r'iain', ProjectViewSet)

class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer

class ProjectSubtitleListAPIView(ListAPIView):
    queryset = ProjectSubtitle.objects.all()
    serializer_class = ProjectSubtitleSerializer
