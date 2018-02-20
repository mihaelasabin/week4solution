"""
week4solution/resume/models.py
Feb 19, 2018
"""
from django.db import models

# Create your models here.
class Resume(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_last_name_first_name(self):
        return "{} {}".format(self.last_name, self.first_name)

    def get_experience(self):
        return self.experience_set.all()

    def get_education(self):
        return self.education_set.all()

class Experience(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=60, null=False, blank=False)
    location = models.CharField(max_length=60, null=False, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=False, blank=True)

    def __str__(self):
    	return self.title

class Education(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
    institution_name = models.CharField(max_length=60, null=False,
    	blank=False)
    location = models.CharField(max_length=60, null=False, blank=True)
    degree = models.CharField(max_length=60, null=False, blank=True)
    major = models.CharField(max_length=60, null=False, blank=True)
    gpa = models.FloatField(null=False, blank=True)

    def __str__(self):
    	return self.institution_name
