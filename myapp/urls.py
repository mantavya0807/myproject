from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.project, name='project'),
    path('education', views.education, name='education'),
    path('contact',views.contact_view, name="contact"),
    path('experience',views.experience, name='experience' ),
    path('projects',views.projects, name='project')
    ]