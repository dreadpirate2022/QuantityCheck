from atexit import register
from django.contrib import admin
from . models import Construction, Tag, Earth, Concrete, Reinforcement, Others, MeasureUnit

# Register your models here.
admin.site.register(Construction)
admin.site.register(Tag)
admin.site.register(Earth)
admin.site.register(Concrete)
admin.site.register(Reinforcement)
admin.site.register(Others)
admin.site.register(MeasureUnit)