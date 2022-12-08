from django.db import models
from apps.blog.models import Skills

# Create your models here.




class Projects(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    additional_link = models.URLField()
    additional_img1 = models.ImageField(default=None, blank=True, null=True)
    skills_learned = models.ManyToManyField(Skills)
    position= models.IntegerField(default=None, null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"