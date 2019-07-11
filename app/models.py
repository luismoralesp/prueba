from django.db import models


"""
Criterios para este modelo:

    - Cada municipio permite guardar los siguientes campos:
        o Código numérico único
        o Texto como nombre del municipio
        o Estado que puede ser Activo o Inactivo
        o Ejemplo de un municipio (código: 5005, nombre: “Santa
        rosa”, estado: Inactivo)
"""
class Municipio(models.Model):
    ACTIVO = 0
    INACTIVO = 1
    ESTADOS = (
        (ACTIVO, 'Activo', ),
        (INACTIVO, 'Inactivo', )
    )
    codigo = models.IntegerField(unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=255)
    estado = models.IntegerField(choices=ESTADOS)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
    
    def __str__(self):
        return self.nombre

"""
Criterios para este modelo:

    - Cada región permite guardar los siguientes campos:
        o Código numérico único
        o Texto como nombre de la región
        o Ejemplo de una región (código: 7, nombre: “Valle de
        aburra”)
"""
class Region(models.Model):
    codigo = models.IntegerField(unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=255)
    """
        Criterios para este campo:
            - Una región contiene municipios y puede tener ninguno o varios municipios asociados
            - Un municipio puede estar en diferentes regiones, por ejemplo el municipio
            “Medellín” puede estar en una región “Andina”, también en una región
            “Valle de aburra”, otra “Latina”, “Paisa”, etc.
            - Los municipios que tienen las regiones solo puede ser municipios con estados activos
    """
    municipios = models.ManyToManyField(Municipio, blank=True, limit_choices_to={ 'estado': Municipio.ACTIVO })
    
    class Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'

    def __str__(self):
        return self.nombre