from django.forms.models import ModelForm

from ChildApp.models import Child

class ChildForm(ModelForm):
     class Meta:
         model = Child
         # todo list all fields
         # fields = model._meta.get_all_field_names()
