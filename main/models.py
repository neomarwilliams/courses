from django.db import models
# from django.contrib import messages

class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Course name must be at least 5 characters long.'
        if len(postData['desc']) < 15:
            errors['desc'] = 'Course description must be at least 15 character long'
        return errors

class Description(models.Model):
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.OneToOneField(Description, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
# Create your models here.
