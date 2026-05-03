from django.urls import path
from .views import ProjectAPI,SkillAPI

urlpatterns = [
    path('projects/', ProjectAPI.as_view()),
    path('skills/', SkillAPI.as_view()),
]