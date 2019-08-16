from django.shortcuts import render
from django.http.response import HttpResponse
# TODO: import Portfolio Model / Project model?

# Create your views here.
def portfolio_view(request):
    # TODO: query all Project models
    # eg. projects = Project.objects.all()
    # TODO: loop through all projects
    return render(request, 'index.html')