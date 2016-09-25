from __future__ import unicode_literals

import datetime
from django.db import models
from django.forms.models import model_to_dict


class Child(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    preferred_name = models.CharField(max_length=30, null=True)
    dob = models.DateField()
    program = models.CharField(max_length=30)
    notes = models.CharField(max_length=100, null=True)

    def serialize(self):
        data = model_to_dict(self)
        # data["caseOfficer"] = self.childcaseofficermap_set().case_officer.serialize()
        return data

class ChildCaseOfficerMap(models.Model):
    child = models.ForeignKey(Child)
    case_officer = models.ForeignKey("UserApp.CaseOfficer")
    case_officer_assigned_start_date = models.DateField(default=datetime.datetime.utcnow().date())
    case_officer_assigned_end_date = models.DateField()


class ChildBlob(models.Model):
    record_key = models.CharField(unique=True,max_length=30)
    record_type = models.CharField(max_length=30)
    record_content = models.BinaryField()
    record_created_at = models.DateField(default=datetime.datetime.utcnow().date())
    record_updated_at = models.DateField(default=datetime.datetime.utcnow().date())
    record_created_by = models.CharField(max_length=30)
    record_updated_by = models.CharField(max_length=30)
