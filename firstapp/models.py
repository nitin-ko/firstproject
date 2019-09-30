from django.db import models

# Create your models here.
class UserRole(models.Model):
    roleId=models.AutoField(primary_key=True)
    roleName=models.CharField(max_length=200,default="")
    isActive=models.BooleanField(default=True)
class SiteUser(models.Model):
    roleId=models.ForeignKey(UserRole,on_delete=models.CASCADE)
    UserFullName=models.CharField(max_length=200,default="")
    UserEmail = models.CharField(primary_key=True,max_length=200, default="")
    UserPassword = models.CharField(max_length=200, default="")
    UserMobile=models.BigIntegerField()
    isActive=models.BooleanField(default=True)
class UserImage(models.Model):
    roleId = models.CharField(max_length=200,default="")
    UserFullName = models.CharField(max_length=200, default="")
    UserEmail = models.CharField(primary_key=True, max_length=200, default="")
    UserPassword = models.CharField(max_length=200, default="")
    UserMobile = models.BigIntegerField()
    UserImage=models.CharField(max_length=200,default="")
    isActive = models.BooleanField(default=True)


