from django import forms
from firstapp.models import SiteUser,UserRole,UserImage
class SiteUserForm(forms.ModelForm):
    class Meta():
        model=SiteUser
        #(fields=='__all__') used here for automatic value
        exclude=["roleId",#this is costumised
                 "UserFullName",
                 "UserMobile",
                 "UserEmail",
                 "UserPassword",
                 "IsActive"]
class UserNameForm(forms.ModelForm):
    class Meta():
        model=UserRole
        exclude=["roleName","roleId"
                 "IsActive"]
class ImageUserForm(forms.ModelForm):
    class Meta():
        model=UserImage
        exclude=["roleId",
                 "UserFullName",
                 "UserMobile",
                 "UserEmail",
                 "UserPassword",
                 "UserImage",
                 "IsActive"]