from django.forms import ModelForm
from django import forms
from promises.models import Promise
 
# define the class of a form
class PromiseForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Promise       
 
        # Custom fields
        fields =["name", "email"]

        labels = {
            "name": "Имя",
            "email": "Почта"
        }
 
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='',
        help_text=''
    )
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'