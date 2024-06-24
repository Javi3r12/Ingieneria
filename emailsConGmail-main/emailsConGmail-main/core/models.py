from django.db import models 

class estadoSoli(models.Model):
    idEstado = models.AutoField(db_column='idEstado', primary_key=True)
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return self.estado
    
class Solicitudes(models.Model):
    id = models.AutoField(primary_key=True)
    idEstado = models.ForeignKey('estadoSoli', on_delete=models.CASCADE, db_column='idEstado', default=1)
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    detalle = models.CharField(max_length=50)
    
    class Meta:      
        ordering = ['id']
