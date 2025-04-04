from django.contrib import admin
from testapp.models import StudentPG,StudentPhd

class StudentPgAdmin(admin.ModelAdmin):
    list_display=['id','Inrollment_no','name','AdharCard','Mobile','Address','course','Gender','Semester','Fee']

admin.site.register(StudentPG,StudentPgAdmin)

class StudentPhdAdmin(admin.ModelAdmin):
    list_display=['id','Inrollment_no','name','AdharCard','Mobile','Address','course','Gender','Semester','Fee']

admin.site.register(StudentPhd,StudentPhdAdmin)
