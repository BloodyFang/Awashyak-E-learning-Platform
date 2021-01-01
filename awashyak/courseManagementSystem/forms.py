from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module

# ModuleFormset helps to work with multiple forms on the same page.
# inlineformset_factory helps to build a model formset dynamically for the Module objects realted to a Course Object.
ModuleFormSet = inlineformset_factory(Course,Module,fields=['title','description'],extra=2,can_delete=True)