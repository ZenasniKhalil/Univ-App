from django.db import models

niveaux = [
    ('L1', 'L1'),
    ('L2', 'L2'),
    ('L3', 'L3'),
    ('M1', 'M1'),
    ('M2', 'M2'),
]

class Domaine(models.Model):
    code = models.CharField(max_length=100,primary_key=True)
    nom = models.CharField(max_length=200)
    def __str__(self):
        return self.nom
    
class Filiere(models.Model):
    code = models.CharField(max_length=100,primary_key=True)
    nom =  models.CharField(max_length=200)
    specialite = models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    mat = models.CharField(max_length=200, primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField()
    domaine = models.ForeignKey(Domaine, on_delete=models.PROTECT)
    filiere = models.ForeignKey(Filiere, on_delete=models.PROTECT)
    niveau = models.CharField(max_length=20, choices=niveaux)
    def __str__(self):
        return self.mat
