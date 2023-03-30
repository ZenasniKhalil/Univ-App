from .models import Etudiant, Domaine, Filiere
import pandas as pd
from datetime import datetime

def importExcel(myfile):       
    dbframe = pd.read_excel(myfile)
    if list(dbframe.columns) == ['Mat. Etudiant',
                                 'Nom',
                                 'Prénom',
                                 'Date de naiss.',
                                 'Code domaine',
                                 'Code filière',
                                 'Code niveau']:
        for dbframe in dbframe.itertuples():
            domaine_instance = Domaine.objects.get(code=dbframe[5])
            filiere_instance = Filiere.objects.get(code=dbframe[6])
            reformating_date = datetime.strptime(dbframe[4], '%d/%m/%Y').date()
            try:
                obj = Etudiant.objects.create(
                    mat=dbframe[1],
                    nom=dbframe[2],
                    prenom=dbframe[3],
                    date_de_naissance=reformating_date,
                    domaine=domaine_instance,
                    filiere=filiere_instance,
                    niveau=dbframe[7]
                )           
                obj.save()
            except:
                pass
    else:
        ## ADD message
        print('Problem in dimantion')
