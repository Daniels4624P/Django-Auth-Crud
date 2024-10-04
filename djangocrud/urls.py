"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import signup, home, tasks, delete_session, signin, create_task, get_task, complete_task, delete_task, tasks_completed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('signup/', signup, name="signup"),
    path('tasks/', tasks, name="tasks"),
    path('tasks/completed/', tasks_completed, name="tasks_completed"),
    path('logout/', delete_session, name="logout"),
    path('signin/', signin, name="signin"),
    path('TaskCreate/', create_task, name="createTask"),
    path('tasks/<int:task_id>/', get_task, name="getTask"),
    path('tasks/<int:task_id>/complete/', complete_task, name="completeTask"),
    path('tasks/<int:task_id>/delete/', delete_task, name="deleteTask")
]
