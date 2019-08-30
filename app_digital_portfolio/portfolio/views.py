from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Project, ProjectSubtitle
import requests
# TODO: import Portfolio Model / Project model?

# Create your views here.
def portfolio_view(request):
    # TODO: query all Project models
    # eg. projects = Project.objects.all()
    # TODO: loop through all projects
    response = requests.get('http://localhost:8000/api/portfolio/?format=json') # 'http://localhost:8000/api/' + request.url + '/?format=json'
    portfolio = response.json()

    return render(request, 'portfolio.html', {"portfolio": portfolio})