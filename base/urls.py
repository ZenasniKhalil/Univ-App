from django.urls import path
from . import views

urlpatterns = [
    path('ajouter-etudiants/', views.addStudent, name='add_student'),
    path('etudiants/', views.student, name='student')
]
