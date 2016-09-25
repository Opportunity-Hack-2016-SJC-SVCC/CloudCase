from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^/caseofficers/<id>/case', views.case_officer_case),
    url(r'^/case/<id>/records', views.get_records_associated_with_case),
    url(r'^/case/<id>/record/<recordkey>/content', views.get_blob_content_of_record)
]