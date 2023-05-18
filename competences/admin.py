from django.contrib import admin
from .models import Direction, Professions, Competence, Standards, Jobs

# Register your models here.
admin.site.register(Direction)
admin.site.register(Professions)
admin.site.register(Competence)
admin.site.register(Standards)
admin.site.register(Jobs)
