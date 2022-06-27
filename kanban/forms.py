from django import forms
from django.contrib.auth.models import User 

from .models import List ,Card

class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)

### リストフォーム
class ListForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = List
        fields = ['title',]

### Card フォーム （新規）
class CardForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Card
        fields = ("title", "description", "list")


### 新規　Card 作成フォーム
class CardCreateFromHomeForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ("title", "description")
