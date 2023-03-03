from django import forms
from .models import Item

CLASS_VARIABLE = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name', 'description', 'image', 'price')
        
        widgets = {
            'category': forms.Select(attrs={
                'class': CLASS_VARIABLE
            }),
            'name': forms.TextInput(attrs={
                'class': CLASS_VARIABLE
            }),
            'Description': forms.Textarea(attrs={
                'class': CLASS_VARIABLE
            }),
            'price': forms.TextInput(attrs={
                'class': CLASS_VARIABLE
            }),
            'image': forms.FileInput(attrs={
                'class': CLASS_VARIABLE
            }),   
        }
    
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'image', 'price', 'is_sold')
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': CLASS_VARIABLE
            }),
            'Description': forms.Textarea(attrs={
                'class': CLASS_VARIABLE
            }),
            'price': forms.TextInput(attrs={
                'class': CLASS_VARIABLE
            }),
            'image': forms.FileInput(attrs={
                'class': CLASS_VARIABLE
            }),   
        }