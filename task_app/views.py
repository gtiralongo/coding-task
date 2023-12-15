from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView


from .models import Task

# Create your views here.


class TaskBaseView(View):
    template_name = 'task.html'
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task:all')


class TaskListView(TaskBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS Task
    """

class TaskDetailView(TaskBaseView,DetailView):
    template_name = "task_detail.html"

class TaskCreateView(TaskBaseView,CreateView):
    template_name = "task_create.html"
    extra_context = {
        "tipo": "Crear tarea"
    }

class TaskUpdateView(TaskBaseView,UpdateView):
    template_name = "task_create.html"
    extra_context = {
        "tipo": "Actualizar tarea"
    }

class TaskDeleteView(TaskBaseView,DeleteView):
    template_name = "task_delete.html"
    extra_context = {
        "tipo": "Borrar tarea"
    }
