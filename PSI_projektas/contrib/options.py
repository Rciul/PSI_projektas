from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType
from django import template
from django.shortcuts import render_to_response

class CustomModelAdmin(ModelAdmin):
    pass