from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class signupform(forms.ModelForm):

    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'First Name'
        }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'last Name'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'example@mingle.com'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder': 'Username','aria-label' : "Username",'aria-describedby' : "basic-addon1"
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'Password'
                }
            )
        }



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image','age','phone','city','state','zip')
        widgets = {
            'image' : forms.ClearableFileInput(
                attrs={
                    'class': 'btn btn-danger btn-sm'
        }
            ),
            'age' : forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'Age'
        }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'phone'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'City'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'State'
                }
            ),
            'zip': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Zip Code'
                }
            )
        }


class signupupdateform(forms.ModelForm):

    class Meta:
        model=User
        fields=('first_name','last_name','email','username')
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'First Name'
        }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'last Name'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'example@mingle.com'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder': 'Username','aria-label' : "Username",'aria-describedby' : "basic-addon1"
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'Password'
                }
            )
        }


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image','age','phone','city','state','zip')
        widgets = {
            'image' : forms.ClearableFileInput(
                attrs={
                    'class': 'imginput'
        }
            ),
            'age' : forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'Age'
        }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'phone'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control','placeholder':'City'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'State'
                }
            ),
            'zip': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Zip Code'
                }
            )
        }