from __future__ import unicode_literals

from django.db import models
from django.forms.models import model_to_dict


class Child(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    preferred_name = models.CharField(max_length=30)
    dob = models.DateField()
    program = models.CharField(max_length=30)
    notes = models.CharField(max_length=100)

    def serialize(self):
        return model_to_dict(self)


class ChildEmployeeMap(models.Model):
    child = models.ForeignKey(Child)
    employee = models.ForeignKey("UserApp.Employee")