from django.db import models

class subiinfo(models.Model):
    city = models.CharField(max_length=8,null=False)
    district = models.CharField(max_length=8,null=False)
    name = models.CharField(max_length=50,null=False)
    tel = models.CharField(max_length=20,null=False)
    addr = models.CharField(max_length=50,null=False)
    owner = models.CharField(max_length=20)
    cel = models.CharField(max_length=20)
    visit_times = models.CharField(max_length=50)
    visit_lastdate = models.DateField()
    def __str__(self):
        return self.name
