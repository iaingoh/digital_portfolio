from portfolio.models import Project, ProjectSubtitle
from rest_framework import routers, serializers, viewsets

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class ProjectSubtitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectSubtitle
        fields = '__all__'

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

router = routers.SimpleRouter()
router.register(r'portfolio', ProjectViewSet)