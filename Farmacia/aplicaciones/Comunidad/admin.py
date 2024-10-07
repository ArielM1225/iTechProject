from django.contrib import admin
from django.utils.html import format_html
from io import BytesIO
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from django.http import HttpResponse
from datetime import date
from aplicaciones.Comunidad.models import Empleado,Proveedor,Paciente,contacto,Laboratorio, provincia, localidad




class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'dni', 'first_name', 'last_name', 'trabajo',  'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'dni', 'trabajo')}),
        ('Contacto', {'fields': ('id_Contacto',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    def generate_chart(self, request, queryset):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [4, 5, 6])
        ax.set_title('Ejemplo de gráfico')

        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        response = HttpResponse(buf.getvalue(), content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename=chart.png'
        return response

    generate_chart.short_description = "Generar gráfico"

    def export_selected_to_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Empleados.pdf"'

        p = canvas.Canvas(response, pagesize=letter)

        pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
        
        p.setFont("Arial-Bold", 12)
        p.drawString(100, 750, "Lista de empleados")
        p.setFont("Arial", 12)
        y = 720
        for item in queryset:
            p.drawString(120, y, f"Empleado: {item.id_Empleado}")
            p.drawString(120, y - 20, f"Nombre: {item.first_name}")
            p.drawString(120, y - 40, f"Apellido: {item.last_name}")
            p.drawString(120, y - 60, f"Dni: {item.dni}")
            p.drawString(120, y - 80, f"Trabajo: {item.trabajo}")
            y -= 120
        p.showPage()
        p.save()
        return response

    export_selected_to_pdf.short_description = "Exportar Empleados seleccionados a PDF"

    actions = [generate_chart, export_selected_to_pdf]

    def calcularEdad(self, obj):
        today = date.today()
        age = today.year - obj.nacimiento.year - ((today.month, today.day) < (obj.nacimiento.month, obj.nacimiento.day))
        return age

    calcularEdad.short_description = 'Edad'

    list_filter = (
        'first_name',
        'last_name',
        'trabajo'
    )

    search_fields = (
        'first_name',
        'last_name',
        'trabajo',
        'dni'
    )

    
class ProveedorAdmin (admin.ModelAdmin):
    list_display=(
        'nombre',
        
    )
    
    list_filter=(
        'nombre',
    )   

class LaboratorioAdmin (admin.ModelAdmin):
    list_display=(
        'nombre',
    )
    
    list_filter=(
        'nombre',
    )   

class PacienteAdmin (admin.ModelAdmin):
    list_display=(
        'nombre',
        'apellido',
        'dni',
    )
    
    
    
    list_filter=(
        'nombre',
        'apellido',
        
    )
    
    search_fields=(
        'nombre',
        'apellido',
        'dni'
    )
    
    def export_selected_to_pdf(modeladmin, request, queryset):
     
         response = HttpResponse(content_type='application/pdf')
         response['Content-Disposition'] = 'attachment; filename="Pacientes.pdf"'

         p = canvas.Canvas(response, pagesize=(595, 842))  # Tamaño A4

         pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
         pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
         
         p.setFont("Arial-Bold", 12)
         p.drawString(100, 750, "Listas de pacientes")
         p.setFont("Arial", 12)
         y = 720
         for item in queryset:
            p.drawString(120, y, f"Paciente: {item.id_Paciente}")
            p.drawString(120, y - 20, f"Nombre: {item.nombre}")
            p.drawString(120, y - 40, f"Apellido: {item.apellido}")
            p.drawString(120, y - 60, f"Dni: {item.dni}")
            y -= 120
         p.showPage()
         p.save()
         return response

    export_selected_to_pdf.short_description = "Exportar Pacientes seleccionados a PDF"
    actions = [export_selected_to_pdf]

class ContactoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Telefono', {
            'fields': ('numero_Telefono', 'numero_Opcional'),
        }),
        ('Dirección', {
            'fields': ('calle', 'número', 'piso', 'departamento', 'localidad', 'código_Postal'),
        }),
        ('Email', {
            'fields': ('email',),
        }),
    )
    
        
class ProvinciaAdmin (admin.ModelAdmin):
    list_display= [
        'nombre',
        ]
    
    list_filter=[
        'nombre',
    ]
    
class LocalidadesAdmin (admin.ModelAdmin):
    list_display= [
        'nombre',
        ]
    
    list_filter=[
        'nombre',
    ]

    
    
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Laboratorio,LaboratorioAdmin)
admin.site.register(contacto, ContactoAdmin)
admin.site.register(provincia, ProvinciaAdmin)
admin.site.register(localidad, LocalidadesAdmin)


