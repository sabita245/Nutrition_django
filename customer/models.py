from django.db import models

# Create your models here.
food_type=(
    ("vegetarian","vegetarian"),
    ("non-vegetarian","non-vegetarian"),
    ("eggiterian","eggiterian"),
)
gender=(
    ("male","male"),
    ("female","female")
)
services=(
    ("Weight Management","Weight Management"),
    ("Sports Nutrition","Sports Nutrition"),
    ("Kids Nutrition","Kids Nutrition"),
    ("Fitness Nutrition","Fitness Nutrition")
)
class CostumerProfile(models.Model):
    customer_name=models.CharField(max_length=100,verbose_name='name',blank=True,null=True)
    customer_age=models.PositiveIntegerField(default=15,verbose_name='age')
    customer_height=models.FloatField(default=5.0,verbose_name='height')
    food=models.CharField(choices=food_type,verbose_name='food',max_length=50,blank=True,null=True)
    gender=models.CharField(max_length=50,choices=gender,verbose_name="gender",blank=True,null=True)
    services=models.CharField(max_length=100,choices=services,null=True,blank=True)





