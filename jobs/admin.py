from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import *

admin.site.unregister(Group)

admin.site.register(JobModel)
admin.site.register(ApplicantModel)
admin.site.register(TagModel)
