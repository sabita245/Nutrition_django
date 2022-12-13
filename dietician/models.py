from django.db import models

# services=(
#     ("Weight Management","Weight Management"),
#     ("Sports Nutrition","Sports Nutrition"),
#     ("Kids Nutrition","Kids Nutrition"),
#     ("Fitness Nutrition","Fitness Nutrition")
# )
feeplan=(
    ("consultion","consultion"),
    ("3Months","3Months"),
    ("1Year","1Year")
)
locations=(
    ("bangalore","bangalore"),
    ("mumbai","mumbai"),
    ("delhi","delhi"),
    ("pune","pune")
)
slot=(
    ("11:00","11:00"),
    ("14:00","14:00"),
    ("16:00","16:00"),
    ("18:00","18:00")
)

class About(models.Model):
    fname=models.CharField(max_length=100,verbose_name="fname",blank=True,null=True)
    lname=models.CharField(max_length=100,verbose_name="lname",blank=True,null=True)
    age=models.PositiveIntegerField(blank=True,null=True,verbose_name="age")
    exp=models.PositiveBigIntegerField(blank=True,null=True,verbose_name="years_of_experience")
    qualification=models.CharField(max_length=100,verbose_name="qualification",blank=True,null=True)
    designation=models.CharField(max_length=100,verbose_name="designation",blank=True,null=True)
    #services=models.CharField(max_length=100,choices=services,null=True,blank=True)

    def __str__(self):
        return str(self.fname)+" "+str(self.lname)
class Fee(models.Model):
    location=models.CharField(max_length=100,choices=locations,verbose_name="location",blank=True,null=True)
    consulting_fee=models.CharField(max_length=100,choices=feeplan,blank=True,null=True,verbose_name="fee")
    booking_date=models.DateField(max_length=100,verbose_name="date",blank=True,null=True)
    booking_time=models.TimeField(max_length=100,choices=slot,verbose_name="time",blank=True,null=True)

class Contact(models.Model):
    city=models.CharField(max_length=100,choices=locations,verbose_name="city",blank=True,null=True)
    address1=models.CharField(max_length=100,verbose_name='address1',blank=True,null=True)
    address2=models.CharField(max_length=100,verbose_name='address2',blank=True,null=True)
    city=models.CharField(max_length=100,choices=locations,verbose_name="city",blank=True,null=True)
    state=models.CharField(max_length=100,verbose_name="state",blank=True,null=True)
    zip_code=models.CharField(max_length=100,verbose_name='zip',blank=True,null=True)
    email=models.EmailField(verbose_name="email")
    
class FAQ(models.Model):
    question=models.CharField(max_length=250,verbose_name="question",blank=True,null=True)
    answer=models.TextField(max_length=1024,verbose_name="answer",blank=True,null=True)
        
