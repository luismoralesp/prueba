from django import forms
from . import models

class MunicipioForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = models.Municipio
    
    """
    Criterios para este método:
        - Si al editar un municipio se pone a estado “Inactivo”, 
        este municipio ya no pertenece a la región (Es decir que la asociación desaparece).
    """
    def save(self, commit=True):
        obj = super().save(commit)
        if obj.estado == models.Municipio.INACTIVO:
            models.Region.municipios.through.objects.filter(municipio=obj).delete()
        return obj

class RegionForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = models.Region