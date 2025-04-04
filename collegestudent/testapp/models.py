from django.db import models

class StudentPG(models.Model):
    Inrollment_no=models.IntegerField(unique=True)
    name=models.CharField(max_length=64,null=False)
    AdharCard=models.BigIntegerField()
    Mobile=models.BigIntegerField()
    Address=models.CharField(max_length=64)
    course=models.CharField(max_length=64,null=False)
    gender_choice=[
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    ]
    Gender=models.CharField(max_length=1,choices=gender_choice)
    Semester=models.IntegerField(null=False)
    Fee=models.FloatField(null=False)
    
class StudentPhd(models.Model):
    Inrollment_no=models.IntegerField(unique=True)
    name=models.CharField(max_length=64,null=False)
    AdharCard=models.BigIntegerField(null=False,unique=True)
    Mobile=models.BigIntegerField(null=False)
    Address=models.CharField(max_length=64,null=False)
    course=models.CharField(max_length=64,null=False)
    gender_choice=[
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    ]
    Gender=models.CharField(max_length=1,choices=gender_choice)
    Semester=models.IntegerField(null=False)
    Fee=models.FloatField(null=False)

class StudentEquery(models.Model):
    Name=models.CharField(max_length=64,null=False)
    Mobile=models.BigIntegerField(null=False)
    Email_id=models.CharField(max_length=64,null=False)
    Course=models.CharField(max_length=64,null=False)
    Address=models.CharField(max_length=64,null=False)



