from django.db import models

# Create your models here.
class matric_app_model(models.Model):
    emis = models.TextField(max_length=100)
    centre_no = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    wrote_2014 = models.TextField(max_length=100)
    passed_2014 = models.TextField(max_length=100)
    wrote_2015 = models.TextField(max_length=100)
    passed_2015 = models.TextField(max_length=100)
    wrote_2016 = models.TextField(max_length=100)
    passed_2016 = models.TextField(max_length=100)
	
	#add an extra field for 'province'
    #province = models.TextField(max_length = 2)
    
    class Meta:
        db_table = "matric_history"