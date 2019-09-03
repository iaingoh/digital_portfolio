from rest_framework.serializers import ModelSerializer

from portfolio.models import Project, ProjectSubtitle, BulletPoint

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectSubtitleSerializer(ModelSerializer):
    class Meta:
        model = ProjectSubtitle
        fields = '__all__'