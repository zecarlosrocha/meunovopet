from django.contrib import admin

from .models import Entidade, Especie, Raca, Animal

admin.site.register(Entidade)
admin.site.register(Especie)
admin.site.register(Raca)
admin.site.register(Animal)
