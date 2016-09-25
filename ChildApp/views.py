from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from ChildApp.models import Child

def dashboard(request):
    return render(request, "index.html")

# def dashboard(request):
#     results = search(cm_list=[])
#     return JsonResponse()

def search(first_name_list=None, middle_name_list=None, last_name_list=None, cm_list=None):
    query = {}
    if first_name_list and isinstance(first_name_list, list):
        query["first_name__in"] = first_name_list
    if middle_name_list and isinstance(middle_name_list, list):
        query["middle_name__in"] = middle_name_list
    if last_name_list and isinstance(last_name_list, list):
        query["last_name__in"] = last_name_list
    if cm_list and isinstance(cm_list, list):
        query["cm_list"] = cm_list
    children = Child.objects.filter(**query)
    
    serialized = []
    for child in children:
        serialized.append(child.serialize())
    return JsonResponse({"query": query, "results": serialized})