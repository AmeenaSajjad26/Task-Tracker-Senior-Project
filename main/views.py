from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Task, Activity
# Create your views here.
def home(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request,'main/home.html',context)
#Task view
class TaskListView(ListView):
    model = Task
    template_name='main/home.html'
    context_object_name = 'tasks'
    ordering =['-duedate']

class TaskDetailView(DetailView):
    model = Task
class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    fields=['taskname','tasktype','duedate']

    def form_valid(self,form):
        form.instance.taskuser = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = Task
    fields=['taskname','tasktype','duedate','spenttime','status']

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

#DoneTask view
def donetask(request):
    context = {
        'donetasks': Task.objects.all()
    }
    return render(request,'main/donetask.html',context)
class DoneTaskListView(ListView):
    model = Task
    template_name='main/donetask.html'
    context_object_name = 'donetasks'
    ordering =['-duedate']


#Activity
def activity(request):
    context = {
        'activitys': Task.objects.all()
    }
    return render(request,'main/activity.html',context)

class ActivityListView(ListView):
    model = Activity
    template_name='main/activity.html'
    context_object_name = 'activitys'

class ActivityDetailView(DetailView):
    model = Activity

class ActivityCreateView(LoginRequiredMixin,CreateView):
    model = Activity
    fields=['activityname','starttime','endtime','repeat']

    def form_valid(self,form):
        form.instance.activityuser = self.request.user
        return super().form_valid(form)

class ActivityUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = Activity
    fields=['activityname','starttime','endtime','repeat']

    def form_valid(self,form):
        form.instance.activityuser = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.activityuser:
            return True
        return False

class ActivityDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Activity
    success_url='/'

    def test_func(self):
        activity = self.get_object()
        if self.request.user == activity.activityuser:
            return True
        return False

#schedule
def schedule(request):
    user_activitys = Activity.objects.get_users_activity(request.user)
    Monschedule=[]
    for x in range(7,20):
        {
            Monschedule.append(Activity.objects.check_activity_time('Mon',x,request.user))
        }
    Tueschedule=[]
    for x in range(7,20):
        {
            Tueschedule.append(Activity.objects.check_activity_time('Tue',x,request.user))
        }
    Wedschedule=[]
    for x in range(7,20):
        {
            Wedschedule.append(Activity.objects.check_activity_time('Wed',x,request.user))
        }
    Thuschedule=[]
    for x in range(7,20):
        {
            Thuschedule.append(Activity.objects.check_activity_time('Thu',x,request.user))
        }
    
    Frischedule=[]
    for x in range(7,20):
        {
            Frischedule.append(Activity.objects.check_activity_time('Fri',x,request.user))
        }
    Satschedule=[]
    for x in range(7,20):
        {
            Satschedule.append(Activity.objects.check_activity_time('Sat',x,request.user))
        }
    Sunschedule=[]
    for x in range(7,20):
        {
            Sunschedule.append(Activity.objects.check_activity_time('Sun',x,request.user))
        }
    context = {
        'tasks': Task.objects.all(),
        'activitys': Activity.objects.all(),
        'user_activitys':user_activitys,
        'range': [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'Monschedule': Monschedule,
        'Tueschedule': Tueschedule, 
        'Wedschedule': Wedschedule, 
        'Thuschedule': Thuschedule, 
        'Frischedule': Frischedule, 
        'Satschedule': Satschedule, 
        'Sunschedule': Sunschedule, 
    }
    return render(request, 'main/schedule.html', context)

