from django.shortcuts import render,redirect
from .importExcel import importExcel 
from .models import Etudiant
from django.contrib import messages
from .forms import FilterForm
from django.db.models import Q

def student(request):
    filter_form = FilterForm()
    table_header = ['Mat. Etudiant',
                    'Nom',
                    'Prénom',
                    'Date de naiss.',
                    'Code domaine',
                    'Code filière',
                    'Code niveau']
    if request.GET.get('mat') != None:
        mat=request.GET.get('mat')
    else:
        mat=''
    if request.GET.get('nom') != None:
        nom=request.GET.get('nom')
    else:
        nom=''
    if request.GET.get('prenom') != None:
        prenom=request.GET.get('prenom')
    else:
        prenom=''
    if request.GET.get('date_de_naissance') != None:
        date_de_naissance=request.GET.get('date_de_naissance')
    else:
        date_de_naissance=''
    if request.GET.get('domaine') != None:
        domaine=request.GET.get('domaine')
    else:
        domaine=''
    if request.GET.get('filiere') != None:
        filiere=request.GET.get('filiere')
    else:
        filiere=''
    if request.GET.get('niveau') != None:
        niveau=request.GET.get('niveau')
    else:
        niveau=''
    print(date_de_naissance)
    students = Etudiant.objects.filter(
        mat__contains=mat,
        nom__contains=nom,
        prenom__contains=prenom,
        domaine__code__contains=domaine,
        niveau__contains=niveau,
        date_de_naissance__contains=date_de_naissance,
        filiere__code__contains=filiere
    )
    context = {
        'students':students,
        'header':table_header,
        'filter_form':filter_form,
    }
    return render(request, 'base/student.html',context)


def addStudent(request):
    if request.method == 'POST':
        if request.FILES.get('myfile'):
            myfile = request.FILES.get('myfile')
            redir = importExcel(request,myfile)
            if(redir):
                return redirect('base:student')
        else:
            messages.error(request, 'Vous n\'avez pas selction un fichier excel !!! ')
    return render(request, 'base/ajouter-etudiants.html')

def deleteStudents(request):
    if request.method == 'POST':
        Etudiant.objects.all().delete()
        return redirect('base:student')
    return render(request, 'base/sup_etudiants.html')




