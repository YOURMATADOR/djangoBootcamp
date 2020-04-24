from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField( required=False,widget=forms.TextInput(attrs={
        "placeholder":"Please enter a title"
    }))
    class Meta:
        model = Product
        fields=["title","description","price","active"]
    # ? if you want some verification for your fields you need you declare a method in the form class with the structure clean_<your_field_name>
    def clean_title(self,*args, **kwargs):
        title = self.cleaned_data.get("title")
        if "pe pe" in title:
            return title
        else:
            raise forms.ValidationError("Please enter a valid title")
        
class ProductFormRaw(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    #? with the widgets you can pass attributes in this case for a textArea i pass a class through out django until the html it self
    description = forms.CharField(max_length=100, required=True,widget=forms.Textarea(attrs={"class":"class-name-example-from-django"}))
    price = forms.DecimalField( required=True)
    active = forms.BooleanField( required=True)