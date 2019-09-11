from rest_framework.serializers import ModelSerializer, SerializerMethodField

from portfolio.models import Project, ProjectSubtitle, BulletPoint

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectDetailSerializer(ModelSerializer):
    subtitles = SerializerMethodField()
    class Meta:
        model = Project
        fields = [
            'title',
            'img',
            'subtitles'
        ]
    
    def get_subtitles(self, obj):
        subtitle_queryset = Project.objects.get_subtitles(obj)
        subtitle_json = SubtitleListSerializer(subtitle_queryset, many=True).data
        print(subtitle_json)
        return subtitle_json

class SubtitleListSerializer(ModelSerializer):
    class Meta:
        model = ProjectSubtitle
        fields = '__all__'