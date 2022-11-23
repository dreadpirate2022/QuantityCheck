from django.forms import ModelForm, widgets
from django import forms
from . models import Construction, Earth, Concrete, Reinforcement, Others

class ConstructionForm(ModelForm):
    class Meta:
        model = Construction
        fields = ['title', 'description', 'featured_image']

        widgets = {
            'tags': forms.SelectMultiple(),
        } 
    
    def __init__(self, *args, **kwargs):
        super(ConstructionForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class':'input'})
        self.fields['title'].widget.attrs.update({'placeholder':'Title between 0 and 30 characters'})
        self.fields['description'].widget.attrs.update({'placeholder':'Description between 0 and 295 characters'})
        self.fields['featured_image'].widget.attrs.update({'class':'featured__image'})

class EarthForm(ModelForm):
    class Meta:
        model = Earth
        fields = ['name', 'custom_name', 'quantity', 'measure_unit']

    def __init__(self, *args, **kwargs):
        super(EarthForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'input'})
        self.fields['custom_name'].widget.attrs.update({'class':'input'})
        self.fields['quantity'].widget.attrs.update({'class':'input'})
        self.fields['measure_unit'].widget.attrs.update({'class':'input'})

class ConcreteForm(ModelForm):
    class Meta:
        model = Concrete
        fields = ['name', 'custom_name', 'quantity', 'measure_unit']

    def __init__(self, *args, **kwargs):
        super(ConcreteForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'input'})
        self.fields['custom_name'].widget.attrs.update({'class':'input'})
        self.fields['quantity'].widget.attrs.update({'class':'input'})
        self.fields['measure_unit'].widget.attrs.update({'class':'input'})

class ReinforcementForm(ModelForm):
    class Meta:
        model = Reinforcement
        fields = ['name', 'custom_name', 'quantity', 'measure_unit']

    def __init__(self, *args, **kwargs):
        super(ReinforcementForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'input'})
        self.fields['custom_name'].widget.attrs.update({'class':'input'})
        self.fields['quantity'].widget.attrs.update({'class':'input'})
        self.fields['measure_unit'].widget.attrs.update({'class':'input'})

class OthersForm(ModelForm):
    class Meta:
        model = Others
        fields = ['name', 'custom_name', 'quantity', 'measure_unit']

    def __init__(self, *args, **kwargs):
        super(OthersForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'input'})
        self.fields['custom_name'].widget.attrs.update({'class':'input'})
        self.fields['quantity'].widget.attrs.update({'class':'input'})
        self.fields['measure_unit'].widget.attrs.update({'class':'input'})