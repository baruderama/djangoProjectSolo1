from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from .forms import CreateNewTask,CreteNewProject


# Create your views here.
def index(request):
    title = 'Django Courser!!'
    return render(request,'index.html',{
        'title':title
    })

def about (request):
    username= 'sebas'
    return render(request,'about.html',{
        'username':username
    })


def hello (request,username):
    print(username)
    return HttpResponse("<h2> hello %s</h2>"% username)



def projects(request):
    # projects=list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects/projects.html',{
        'projects': projects
    })
    # return JsonResponse(projects,safe=False)

def tasks(request):
    # las dos lineas de abajo hacen los mismo de encontrar un onjeto por id pero la segunda da un mensaje
    # si no existe
    # task=Task.objects.get(id=id)
    # task= get_object_or_404(Task,id=id)
    tasks = Task.objects.all()
    
    return render(request,'tasks/tasks.html',{
        'tasks':tasks
    })
    # return HttpResponse('tasks: %s'% task.title)
    
def create_task(request):
    # print(request.GET)
    if request.method == 'GET':
        return render(request,'tasks/create_task.html',{
            'form':CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'],project_id=2
                            )
        return redirect ('tasks')
    # Task.objects.create(
    #     title=request.GET['title'],
    #     description=request.GET['description'],
    #     projectkey=2
    #                     )
    # return render(request, 'create_task.html',{
    #     'form': CreateNewTask()
    # })
       
    
def create_project(request):
    if request.method == 'GET':
        return render(request,'projects/create_project.html',
                  
                  {'form': CreteNewProject()}
                  )
    else:
        Project.objects.create(name=request.POST['name'],
                            )
        return redirect ('/projects/')
    