from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project,Skill

class ProjectAPI(APIView):
    def get(self, request):
        projects = Project.objects.all()

        data = []
        for p in projects:
            data.append({
                "title": p.title,
                "image": request.build_absolute_uri(p.image.url) if p.image else "",
                "github": p.github,
                "live": p.live,
            })

        return Response(data)
class SkillAPI(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        data = []

        for s in skills:
            data.append({
                "title": s.title,
                "image": request.build_absolute_uri(s.image.url) if s.image else ""
            })

        return Response(data)