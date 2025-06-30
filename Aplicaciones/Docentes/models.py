from django.db import models

class Docente(models.Model):
    ESTADO_CHOICES = [('Activo', 'Activo'),('Inactivo', 'Inactivo'),]
    idDocente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    gradoAcademico = models.CharField(max_length=100)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    fechaNacimeinto = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    def __str__(self):
        fila = "{0}: {1} {2} {3}"
        return fila.format(self.idDocente, self.nombre, self.apellido, self.gradoAcademico)




class Cargo(models.Model):

    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    funciones=models.TextField()
    horario=models.CharField(max_length=500)
    requisitos=models.TextField()
    sueldo=models.DecimalField(max_digits=10,decimal_places=2)
    logo = models.FileField(upload_to='Docentes',null=True, blank=True )




    def __str__(self):
        fila="{0}: {1} {2} {3}"
        return fila.format(self.id,self.nombre,self.sueldo,self.horario)
    
