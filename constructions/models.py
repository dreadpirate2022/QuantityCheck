from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Construction(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True, max_length=295)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    @property
    def imageURL_constructions(self):
        try:
            url = self.featured_image.url
        except:
            url = 'static/images/default.jpg'

        return url

    @property
    def imageURL_single_construction(self):
        try:
            url = self.featured_image.url
        except:
            url = '/static/images/default.jpg'

        return url

class Tag(models.Model):
    name = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

class Earth(models.Model):
    owner = models.ForeignKey(Construction, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    name = models.CharField(max_length=50, default='Position Name')
    custom_name = models.CharField(max_length=50, default='Position Custom Name')
    quantity = models.DecimalField(decimal_places=2, max_digits=50, null=True, blank=True, default=0)
    # measure_unit = models.CharField(max_length=10, null=True, blank=True)
    measure_unit_dropdown = models.ForeignKey('MeasureUnit', null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']        

class Concrete(models.Model):
    owner = models.ForeignKey(Construction, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    name = models.CharField(max_length=50, default='Position Name')
    custom_name = models.CharField(max_length=50, default='Position Custom Name')
    quantity = models.DecimalField(decimal_places=2, max_digits=50, null=True, blank=True, default=0)
    # measure_unit = models.CharField(max_length=10, null=True, blank=True)
    measure_unit_dropdown = models.ForeignKey('MeasureUnit', null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']

class Reinforcement(models.Model):
    owner = models.ForeignKey(Construction, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    name = models.CharField(max_length=50, default='Position Name')
    custom_name = models.CharField(max_length=50, default='Position Custom Name')
    quantity = models.DecimalField(decimal_places=2, max_digits=50, null=True, blank=True, default=0)
    # measure_unit = models.CharField(max_length=10, null=True, blank=True)
    measure_unit_dropdown = models.ForeignKey('MeasureUnit', null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

class Others(models.Model):
    owner = models.ForeignKey(Construction, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    name = models.CharField(max_length=50, default='Position Name')
    custom_name = models.CharField(max_length=50, default='Position Custom Name')
    quantity = models.DecimalField(decimal_places=2, max_digits=50, null=True, blank=True, default=0)
    # measure_unit = models.CharField(max_length=10, null=True, blank=True)
    measure_unit_dropdown = models.ForeignKey('MeasureUnit', null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

class MeasureUnit(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
