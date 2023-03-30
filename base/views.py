from django.shortcuts import render
from .importExcel import importExcel 
from .models import Etudiant

def student(request):
    students = Etudiant.objects.all()
    table_header = ['Mat. Etudiant',
                    'Nom',
                    'Prénom',
                    'Date de naiss.',
                    'Code domaine',
                    'Code filière',
                    'Code niveau']
    context = {
        'students':students,
        'header':table_header,
    }
    return render(request, 'base/student.html',context)


def addStudent(request):
    if request.method == 'POST':
        if request.FILES.get('myfile'):
            myfile = request.FILES.get('myfile')
            importExcel(myfile)
        else:
            print('haaa rah 5awi ya wed 3ami')
    return render(request, 'base/ajouter-etudiants.html')
