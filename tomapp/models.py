#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Programme (models.Model):
    Domaine = models.CharField(choices=[('E&G','Economie et Gestion'),('S&T','Sciences et Technologiques')],max_length=50)
    Mention = models.CharField(choices=[('E&G','Economie et Gestion'),('SI','Sciences informatiques')],max_length=50)
    Specialite = models.CharField(choices=[('Tél','Télécommunications'),('BDD','Base de données'),('ONE','Organisation de la net Economie'),('NOSP','NOSP'),('SdE','Sciences entreprise'),('SC','Sciences Comptables')],max_length=50)
    TypeCours = models.CharField(choices=[('OPT','Optionnel'),('OBLI','Obligatoire')],max_length=50)
    Langue = models.CharField(choices=[('EN','Anglais'),('FR','Francais')],max_length=50)
    def __unicode__(self):
        return u'%s-%s-%s-%s-%s' % (self.Domaine,self.Mention,self.Specialite,self.TypeCours,self.Langue)


class Cours (models.Model):
    program = models.ForeignKey('Programme')
    Etablissement = models.CharField(max_length=50)
    Grade = models.CharField(choices=[('Propédeutique','Propédeutique'),('L1','L1'),('L2','L2'),('L3','L3'),('Master','Master')],max_length=50)
    Semestre = models.CharField(choices=[('Y','Y'),('S1','S1'),('S2','S2')],max_length=50)
    NomCours = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s-%s-%s-%s-%s' % (self.program,self.Etablissement,self.Grade,self.Semestre,self.NomCours)


class Professeurs (models.Model):
    NomProfesseur = models.CharField(max_length=20)
    PrenomProfesseur = models.CharField(max_length=20)
    Tel = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50)
    Adresse = models.CharField(max_length=50)
    CINP = models.CharField(max_length=25)
    def __unicode__(self):
        return u'%s'% (self.NomProfesseur)

class DescriptionCours (models.Model):
     cours = models.ForeignKey('Cours')
     professeurs = models.ManyToManyField('Professeurs')
     CodeCours = models.CharField(max_length=50)
     NomCours = models.CharField(max_length=50)
     CrediEcts = models.IntegerField(max_length=10)
     Etablissement = models.CharField(max_length=20)
     PublicCible = models.CharField(max_length=20)
     PreRequis = models.CharField(max_length=100)
     Objectif = models.CharField(max_length=100)
     Description = models.CharField(max_length=50)
     PlanCours = models.CharField(max_length=200)
     Format = models.CharField(max_length=50)
     Ressource = models.CharField(max_length=50)
     Evalution = models.CharField(max_length=50)
     def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.cours,self.professeurs,self.CodeCours,self.NomCours,self.CrediEcts,self.Etablissement,self.PublicCible,self.PreRequis,self.Objectif,self.Description,self.PlanCours,self.Format,self.Ressource,self.Evalution)


class CV(models.Model):
    professeurs = models.ForeignKey('Professeurs')
    DateN = models.DateField()
    LieuN = models.CharField (max_length=100)
    Tel2 = models.CharField(max_length=15)
    EtatC = models.CharField(max_length=20)
    ExpP = models.CharField(max_length=400)
    DateE = models.DateField()
    FormationA = models.CharField(max_length=400)
    DateF = models.DateField()
    Specialite = models.CharField(max_length=500)
    Reference = models.CharField(max_length=400)
    Langue = models.CharField(max_length=20)
    def __unicode__(self):
        return u'%s %s %s %s %s %s' % (self.professeurs,self.DateN,self.LieuN,self.Tel2,self.EtatC,self.ExpP,self.DateE,self.FormationA,self.DateF,self.specialite,self.Reference,self.Langue)








