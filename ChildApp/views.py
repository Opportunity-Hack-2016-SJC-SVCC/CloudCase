from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "MyBriefcaseLoginPage.html")

def jsonResponse(request):
    return JsonResponse({"name" : "nishanth"})