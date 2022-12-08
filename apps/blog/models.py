from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Skills(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    additional_link = models.URLField()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skills"

class AwardingInstitutions(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    website = models.URLField()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Awarding Institutions"

class CourseraCertifications(models.Model):
    id = models.AutoField(primary_key=True)
    awarding_institution = models.ForeignKey(AwardingInstitutions, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    img = models.ImageField(blank=True, null=True, default=None)
    skills_learned = models.ManyToManyField(Skills)
    topic_1 = models.TextField(max_length=500)
    topic_2 = models.TextField(max_length=500)
    topic_3 = models.TextField(max_length=500)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Coursera Certifications"