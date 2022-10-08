from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('priorities/', views.PriorityList.as_view()),
    path('priorities/<int:pk>/', views.PriorityDetail.as_view()),
    path('groups/', views.GroupList.as_view()),
    path('groups/<int:pk>/', views.GroupDetail.as_view()),
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
