from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


# Users = get_user_model()


class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢', min_value=0)
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ('username', 'age', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        # パスワードが正しいかチェック
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません')
    
    def save(self, commit=False):
        user = super().save(commit=False)
        # パスワードの暗号化と保存
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class LoginForm(forms.Form):
    email = forms.CharField(label="メールアドレス")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput())

class UserEditForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢', min_value=0)
    email = forms.EmailField(label='メールアドレス')
    picture = forms.FileField(label='写真', required=False)

    class Meta:
        model = Users
        fields = ('username', 'age', 'email', 'picture')


class PasswordChangeForm(forms.ModelForm):

    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())
    
    class Meta():
        model = Users
        fields = ('password', )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが異なります')

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user




# class UserCreationForm(forms.ModelForm):
#     password = forms.CharField(label='password', widget=forms.PasswordInput())
#     confirm_password = forms.CharField(label='Password再入力', widget=forms.PasswordInput())

#     class Meta:
#         model = Users
#         fields = ('username', 'age', 'email', 'password') # 作成時に表示するフィールド
    
#     def clean(self):
#         cleaned_data = super().clean()
#         # パスワードが正しいかチェック
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')
#         if password != confirm_password:
#             raise ValidationError('パスワードが一致しません')

#     def save(self, commit=False):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data.get("password"))
#         user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()
#     # website = forms.URLField(required=False)
#     picture = forms.FileField(required=False)

#     class Meta:
#         model = Users
#         fields = ('username', 'age', 'email', 'password', 'is_staff', 'is_active', 'is_superuser', 'picture')
    
#     def clean_password(self):
#         # すでに登録されているパスワードを返す
#         return self.initial['password']

