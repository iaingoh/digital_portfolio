from django.urls import path
from portfolio.api.views import (
    ProjectDetailAPIView,
    ProjectListAPIView,
    ProjectSubtitleListAPIView
)

urlpatterns = [
    path('', ProjectListAPIView.as_view(), name="portfolio_api"),
    path('<pk>/', ProjectDetailAPIView.as_view(), name="project-detail")
]
