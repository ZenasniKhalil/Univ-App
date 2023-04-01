from django.urls import path
from . import views
app_name='base'
urlpatterns = [
    path('ajouter-etudiants/', views.addStudent, name='add_student'),
    path('etudiants/', views.student, name='student'),
    path('sup_etudiants/', views.deleteStudents, name='sup_etudiants'),
]
