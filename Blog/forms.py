from django import forms
from .models import Blog,Product
class BlogForm(forms.ModelForm):

    class Meta:
       model=Blog
       fields='__all__'

class ProductForm(forms.ModelForm):
    
    class Meta:
        model=Product
        fields='__all__'

    def _init__(self,*args, **kwargs):
        super(ProductForm, self)._init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
            self.fields[field].required = False




