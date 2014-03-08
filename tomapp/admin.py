from django.contrib import admin
from tomapp.models import Professeurs, Programme, Cours, DescriptionCours, CV

admin.site.register(Professeurs)
admin.site.register(Programme)
admin.site.register(Cours)
admin.site.register(DescriptionCours)
admin.site.register(CV)
# Register your models here.
