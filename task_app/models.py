from django.db import models
from django.db.models import Model


# Create your models here.
class Task(Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model
    """

    nombre = models.CharField(max_length=100, default="Debugear")
    rubro = models.CharField(max_length=100, default="Test", blank=False, null=False)
    # contacto = models.EmailField(max_length=100, default="no_contact@mail.com")
    # ubicacion = models.CharField(max_length=100, default="Tienda online")
    fecha_habilitacion = models.DateField(blank=False, null=False, auto_now=True)

    # podemos crear la tabla con un nombre especifico pero se lo tenemos
    # que indicar directamente en la metaclase

    class Meta:
       db_table = "coding_task"


    def __str__(self):
        return f"El nombre de la tarea: {self.nombre} rubro: {self.rubro}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]


# -> Next registrar modelo admin.py