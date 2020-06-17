from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from .models import Task
# Create your views here.
def home(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request,'main/home.html',context)

class TaskListView(ListView):
    model = Task
    template_name='main/home.html'
    context_object_name = 'tasks'
    ordering =['-duedate']

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    fields=['taskname','tasktype','duedate','estimatetime']

    def form_valid(self,form):
        form.instance.taskuser = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = Task
    fields=['taskname','tasktype','duedate','estimatetime']

    def form_valid(self,form):
        form.instance.taskuser = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.taskuser:
            return True
        return False

class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Task
    success_url='/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.taskuser:
            return True
        return False