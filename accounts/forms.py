###### アカウント作成用
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


###### ログイン用
from django.contrib.auth.forms import AuthenticationForm


######### ユーザー作成用 フォーム
class UserCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #htmlの表示を変更可能にします (form-control) クラスを付与
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model  = User
        fields = ("username", "password1", "password2")

###### ログイン用　フォーム
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)

       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'