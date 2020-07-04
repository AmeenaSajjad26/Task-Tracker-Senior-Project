from django.urls import path
from .views import (TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView,TaskDeleteView,
ActivityListView, ActivityDetailView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView,
DoneTaskListView)
from . import views
urlpatterns = [
    path('', views.stats,name='main-stat'),
    path('task/', TaskListView.as_view(),name='main-home'),
    path('donetask/', DoneTaskListView.as_view(),name='main-donetask'),
    path('task/<int:pk>/', TaskDetailView.as_view(),name='task-detail'),
    path('task/new/', TaskCreateView.as_view(),name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(),name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(),name='task-delete'),

    path('activity/', ActivityListView.as_view(),name='main-activity'),
    path('activity/<int:pk>/', ActivityDetailView.as_view(),name='activity-detail'),
    path('activity/new/', ActivityCreateView.as_view(),name='activity-create'),
    path('activity/<int:pk>/update/', ActivityUpdateView.as_view(),name='activity-update'),
    path('activity/<int:pk>/delete/', ActivityDeleteView.as_view(),name='activity-delete'),
    path('schedule/', views.schedule,name='schedule'),
]
