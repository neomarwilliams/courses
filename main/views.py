from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def course_list(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses.html', context)

def create_course(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')
        
    else:
        this_desc=Description.objects.create(
            desc=request.POST['desc']
        )
        this_course=Course.objects.create(
            name=request.POST['name'],
            desc=this_desc
        )
        return redirect('/')

def one_course_view(request, id):
    this_course=Course.objects.get(desc_id=id)
    context={
        'name':this_course.name,
        'desc':this_course.desc.desc,
        'id':this_course.desc_id
    }
    return render(request, 'delete_course.html', context)

def delete_course(request, id):
    delete_me=Course.objects.get(desc_id=id)
    delete_me.delete()
    return redirect('/')

# Fix it list
# capture id from the course created in the for loops. For some reason it is not capturing...
