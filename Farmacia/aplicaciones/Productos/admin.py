from django.contrib import admin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from aplicaciones.Productos.models import Producto
from django.utils.html import format_html

class ProductosAdmin (admin.ModelAdmin):
    list_display=(
        'nombre_Comercial',
        'tipo_Producto',
        'stock',
        'id_Laboratorio'
    )
    
    list_filter=(
        'nombre_Comercial',
        'principio_activo',
        'tipo_Producto'
        
    ) 
    
    # def mostrar_stock(self, obj):
    #     return calcular_stock(obj.id_producto) 

    # mostrar_stock.short_description = 'Stock Actual'
    
    def export_selected_to_pdf(modeladmin, request, queryset):
     
         response = HttpResponse(content_type='application/pdf')
         response['Content-Disposition'] = 'attachment; filename="Productos.pdf"'

         p = canvas.Canvas(response, pagesize=(595, 842))  # Tamaño A4

         pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
         pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
         
         p.setFont("Arial-Bold", 12)
         p.drawString(100, 750, "Listas de pacientes")
         p.setFont("Arial", 12)
         y = 720
         for item in queryset:
            p.drawString(120, y, f"Producto: {item.id_producto}")
            p.drawString(120, y - 20, f"Nombre: {item.nombre_Comercial}")
            p.drawString(120, y - 40, f"Droga: {item.principio_activo}")
            p.drawString(120, y - 60, f"Presentacion: {item.presentacion}")
            p.drawString(120, y - 80, f"Accion: {item.accion_farma}")
            p.drawString(120, y - 80, f"Tipo de producto: {item.tipo_Producto}")
            p.drawString(120, y - 120, f"Stock: {item.stock}") # Mostrar el stock del producto
            y -= 120
         p.showPage()
         p.save()
         return response

    export_selected_to_pdf.short_description = "Exportar Movimientos seleccionados a PDF"
    actions = [export_selected_to_pdf]
     

admin.site.register(Producto,ProductosAdmin)

