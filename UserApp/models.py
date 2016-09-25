from __future__ import unicode_literals

import datetime
from django.db import models
from django.contrib.auth.models import User


class CaseOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.datetime.utcnow().date())
    date_relieved = models.DateField(null=True)