from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Products


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['image']

# class ProductCreateForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name','base_price','description','image']




class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'base_price', 'live_until', 'description', 'image']
        widgets = {
            'live_until': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['current_price']

        