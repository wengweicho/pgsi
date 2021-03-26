from django.db import models
class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.FileField(upload_to = 'pictures')
   class Meta:
      db_table = "profile"
class UploadFiles(models.Model):
#     jobrole = models.CharField(max_length=100)
    upload_files = models.FileField(upload_to='mysite/', blank=True, null=True)
