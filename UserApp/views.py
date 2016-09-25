from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http.response import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
def login_user(request):
    user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
    if user is not None:
        login(request, user)
        return JsonResponse({"id":user.pk, "next": reverse("caseofficer-dashboard")})
    else:
        return JsonResponse({"error": "Invalid Credentials"})