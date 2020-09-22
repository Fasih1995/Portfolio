from django.shortcuts import render

# Create your views here.
from muneebulhassan.models import project, experience


def index(request):
    projects = project.objects.all
    exp = experience.objects.all
    # exp = {'experience': exps }
    parms ={'project' : projects, 'experience': exp }
    return render(request, "index.html",parms)




# def add(request):
#     name = request.GET['username']
#     project = request.GET['project']
#     print(name + "  this is pasd " + project)
#     return render(request, "index.html")
