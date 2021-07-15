from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list),
    path('courses/create', views.create_course),
    path('courses/update/<int:id>', views.one_course_view),
    path('courses/destroy/<int:id>', views.delete_course),
]