from django.shortcuts import render,redirect
from .importExcel import importExcel 
from .models import Etudiant,Verifier, Domaine, Filiere
from django.contrib import messages
from .forms import DomaineForm, FiliereForm
from .filters import EtudiantFilter, VerifierFilter
from django.db import IntegrityError

def dashboard(request):
    table_header = ['Mat. Etudiant',
                    'Nom',
                    'Prénom',
                    'Date de naiss.',
                    'Code domaine',
                    'Code filière',
                    'Code niveau',
                    'Date de l\'examen',
                    'Heure de l\'examen']
    records = VerifierFilter(request.GET, queryset=Verifier.objects.all())
    context={
        'records':records,
        'header':table_header
    }
    return render(request, 'base/records.html', context)

def student(request):
    table_header = ['Mat. Etudiant',
                    'Nom',
                    'Prénom',
                    'Date de naiss.',
                    'Code domaine',
                    'Code filière',
                    'Code niveau']
    students = EtudiantFilter(request.GET, queryset=Etudiant.objects.all())
    context = {
        'students':students,
        'header':table_header,
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


def addDomaine(request):
    form = DomaineForm()
    if request.method == 'POST':
        try:
            Domaine.objects.create(
                code=request.POST.get('code'),
                nom=request.POST.get('nom')
            )
            return redirect('base:dashboard')
        except IntegrityError as e:
            messages.error(request, 'Le Code <strong>'+str(request.POST.get('code'))+'</strong> est deja existant !!!')
        
    context={
        'form':form
    }
    return render(request, 'base/domaine.html',context)




