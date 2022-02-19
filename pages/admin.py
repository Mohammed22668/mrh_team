from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Project)
# admin.site.register(Rusul)
# admin.site.register(Hussain)
# admin.site.register(Mohammed)
admin.site.register(Members)
admin.site.register(Posts)
