from django.urls import path
from portfolio.api.views import (
    ProjectListAPIView,
    ProjectSubtitleListAPIView
)

urlpatterns = [
    path('', ProjectListAPIView.as_view(), name="portfolio_api"),
    path('<project_id>/', ProjectSubtitleListAPIView.as_view(), name="portfolio_api")
]
