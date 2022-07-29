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
 
    # this function will be used for the validation
    def clean(self):
 
        # data from the form is fetched using super function
        super(PromiseForm, self).clean()
         
        # extract the username and text field from the data
        username = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
 
        # conditions to be met for the username length
        # if not username:
        #     self._errors['username'] = self.error_class([
        #         'Name is required'])
        # if not email:
        #     self._errors['text'] = self.error_class([
        #         'Email is required'])
 
        # return any errors if found
        return self.cleaned_data