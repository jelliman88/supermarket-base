from django.db import models


class Part(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100, blank=True)
    danish_slug = models.CharField(max_length=100, blank=True)
    part_no = models.IntegerField(null=True, blank=True)
    part_group = models.CharField(max_length=50, blank=True)
    item_no = models.IntegerField(null=True, blank=True)
    group_no = models.IntegerField(null=True, blank=True)
    bike_models = models.JSONField(default=list, blank=True)
    out_of_stock = models.BooleanField(default=False)
    expected_date = models.DateField(null=True, blank=True)
    inactive = models.BooleanField(default=False)




class ExcelSheet(models.Model):
    upload_date = models.DateTimeField(auto_now=True)
    data = models.JSONField(default=list)


    
