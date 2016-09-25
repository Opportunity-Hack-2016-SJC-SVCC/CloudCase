from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from ChildApp.forms import ChildForm
from ChildApp.models import Child
from ChildApp.models import ChildCaseOfficerMap

def dashboard(request):
    # todo login. No anonymous user. No pk fopr him
    return JsonResponse(get_list_cases_associated_with_case_officer(request.user.pk))


def case_officer_case(request):
    if request.method == 'GET':
        return get_list_cases_associated_with_case_officer(request)
    elif request.method == 'POST':
        return create_case_associated_with_case_officer(request)


def get_list_cases_associated_with_case_officer(case_officer_id):
    return search(cm_list=[case_officer_id])

def create_case_associated_with_case_officer(request):
    data = request.POST
    form = ChildForm(data)
    if (form.is_valid()):
        child = form.save()
        return JsonResponse({'id': child.pk})
    else:
        return JsonResponse({'errors': form.errors})


# return only meta like record_name, record_cat, record_type, created_at, created_by...
def get_records_associated_with_case(request):
    return JsonResponse()


# return blob content
def get_blob_content_of_record(request):
    return JsonResponse()


def create_records_associated_with_case(request):
    return JsonResponse()


def search(first_name_list=None, middle_name_list=None, last_name_list=None, cm_list=None):
    query = {}
    if first_name_list and isinstance(first_name_list, list):
        query["first_name__in"] = first_name_list
    if middle_name_list and isinstance(middle_name_list, list):
        query["middle_name__in"] = middle_name_list
    if last_name_list and isinstance(last_name_list, list):
        query["last_name__in"] = last_name_list
    if cm_list and isinstance(cm_list, list):
        pass
    children = Child.objects.filter(**query)
    
    serialized = []
    for child in children:
        serialized.append(child.serialize())
    return {"query": query, "results": serialized}