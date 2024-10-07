from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from django.contrib.auth.hashers import make_password


class Empleado(AbstractUser):
    JOB_CHOICES = (
        ('auxiliar', 'Auxiliar'), 
        ('administrativo', 'Administrativo'),
        ('farmacéutico', 'Farmacéutico'),
        ('médico', 'médico'),
    )

    dni = models.IntegerField('Dni', unique=True, null=True, blank=True)
    trabajo = models.CharField('Puesto', max_length=20, choices=JOB_CHOICES)
    nacimiento = models.DateField('Nacimiento', default=date.today)
    id_Contacto = models.ForeignKey('Comunidad.contacto', null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        unique_together = ('first_name', 'last_name', 'dni')
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]

    def save(self, *args, **kwargs):
        # Si la contraseña no está encriptada, la encriptamos antes de guardarla
        if self.pk is None or 'pbkdf2_sha256$' not in self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.last_name} - {self.first_name}'
    
    

class Paciente (models.Model): 
    id_Paciente = models.AutoField(primary_key=True)
    nombre= models.CharField ('Nombre',max_length=17)   
    apellido = models.CharField ('Apellido',max_length=50)
    dni= models.IntegerField ('Dni')
    id_Contacto = models.ForeignKey('Comunidad.contacto', on_delete=models.CASCADE, verbose_name= 'Información de contacto')
    
    class Meta:
        verbose_name= 'Paciente'
        verbose_name_plural='Pacientes'
        unique_together=('nombre','apellido','dni')
    
    def __str__(self):
        return self.nombre + '  ' + self.apellido 
    
class Proveedor (models.Model): 
    
    RAZON_SOCIAL_CHOICES = [
        ('SA', 'Sociedad Anónima'),
        ('SRL', 'Sociedad de Responsabilidad Limitada'),
        ('SAS', 'Sociedad por Acciones Simplificada'),
        ('Cooperativa', 'Cooperativa'),
        ('Monotributista', 'Monotributista'),
        ('Autónomo', 'Autónomo'),
        # Agrega más opciones según sea necesario
    ]
    
    id_Proveedor = models.AutoField(primary_key=True)
    nombre= models.CharField ('Nombre',max_length=17)   
    r_Social = models.CharField('Razón Social', max_length=50, choices=RAZON_SOCIAL_CHOICES)
    id_Contacto = models.ForeignKey('Comunidad.contacto', on_delete=models.CASCADE, verbose_name= 'Información de contacto')
    
    class Meta:
        verbose_name= 'Proveedor'
        verbose_name_plural='Proveedores'
        unique_together=('nombre','r_Social')
    
    def __str__(self):
        return self.nombre 

class Laboratorio(models.Model):
    id_Laboratorio=models.AutoField(primary_key=True, verbose_name='Laboratorio')
    nombre = models.CharField(max_length=100)
    
    
    class Meta:
        verbose_name = 'Laboratorio'
        verbose_name_plural = 'Laboratorios'
        

    def __str__(self):
        return self.nombre


class contacto (models.Model):
    JOB_CHOICES = (
        ('Auxiliar', 'Auxiliar'), 
        ('Administrativo', 'Administrativo'),
        ('Farmaceutico', 'Farmaceutico'),
        ('Medico', 'Medico'),
    )
    id_Contacto=models.AutoField(primary_key=True)
    numero_Telefono=models.IntegerField ('Número telefónico',null=True)
    numero_Opcional= models.IntegerField ('Numero alternativo',null=True, blank= True)
    email = models.CharField('Correo electrónico',max_length=50,)
    calle=models.CharField ('Calle',max_length=50)
    número=models.IntegerField ('Numero')
    piso=models.IntegerField ('N° Piso',null=True, blank=True)
    departamento=models.CharField ('Departamento',max_length=50,null=True, blank=True)
    localidad=models.ForeignKey('Comunidad.localidad',null=True, on_delete=models.CASCADE)
    código_Postal=models.IntegerField ('Codigo Postal',null=True)

class provincia (models.Model):
    id_Provincia=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class localidad (models.Model):
    id_Localidad=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    Id_provincia= models.ForeignKey('Comunidad.provincia',null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre}, {self.Id_provincia.nombre if self.Id_provincia else 'Provincia no asignada'}"

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'