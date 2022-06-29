from django.shortcuts import render
from projects.models import Project
# Create your views here.

# View for project index
def project_index(request):
    # Retrieve all objects from projects table
    projects = Project.objects.all()
    # Defines context dictionary to be used to send information to our template
    # Every view function created needs to have a context dictionary
    context = {
        'projects': projects
    }
    # Return a response where you render the response from request, the template & the context
    return render(request, 'project_index.html', context)

# View for project details
def project_detail(request, pk):
    # Get the object by primary key from request
    project = Project.objects.get(pk=pk)
    # Defines context dictionary
    context= {
        'project': project
    }
    return render(request, 'project_detail.html', context)
