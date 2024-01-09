from django.shortcuts import render

# Create your views here.
def futureJob(request):
    return render(request, "future_job.html")

def futureJobSkill(request):
    return render(request, "future_job_skill.html")

def futureJobMedia(request):
    return render(request, "future_job_media.html")