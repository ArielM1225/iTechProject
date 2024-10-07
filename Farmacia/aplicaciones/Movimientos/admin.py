from django.contrib import admin
from aplicaciones.Movimientos.models import Entrada, Salida, SalidaProducto, EntradaProducto, AjusteProducto,AjusteStock, HistorialMovimiento

class EntradaProductoInline(admin.TabularInline):
    model = EntradaProducto
    extra = 1
    

class SalidaProductoInline(admin.TabularInline):
    model = SalidaProducto
    extra = 0
    can_delete = False
    readonly_fields = ['producto', 'cantidad']
    
    
class EntradaAdmin (admin.ModelAdmin):
    inlines = [EntradaProductoInline,]
    list_display=(
        'id_Proveedor',
        'id_Entrada',
        'created_at',
        )

   
    
class SalidaAdmin(admin.ModelAdmin):
    inlines = [SalidaProductoInline]  # Usamos el inline para mostrar los productos en la Salida
    list_display = ('id_Paciente', 'id_Salida', 'created_at', 'entregado')
    list_filter = ('entregado', 'created_at')

    def get_readonly_fields(self, request, obj=None):
        # Si el objeto ya existe (es una edición), solo permitimos editar el campo 'entregado'
        if obj:
            return ['id_Paciente', 'id_Salida', 'productos', 'created_at', 'recetas', 'duplicado']  # Otros campos como solo lectura
        else:
            return []

    def has_delete_permission(self, request, obj=None):
        # Desactivar la opción de eliminar
        return False
    
    
    
    
class AjusteProductoInline(admin.TabularInline):
    model = AjusteProducto
    extra = 1  # Número de formularios adicionales vacíos

# Configuración del admin para AjusteStock
class AjusteStockAdmin(admin.ModelAdmin):
    inlines = [AjusteProductoInline,]  # Inline para gestionar los productos dentro del ajuste
    list_display = (
        'id_ajuste',
        'motivo',
        'created_at',
    )
    search_fields = ['id_ajuste', 'motivo']  # Campos para búsqueda
    list_filter = ['created_at']  # Filtro por fecha de creación
    
    
class HistorialMovimientoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'tipo_movimiento', 'cantidad', 'fecha_movimiento', 'motivo')
    list_filter = ('tipo_movimiento', 'fecha_movimiento')
    search_fields = ('producto__nombre_Comercial', 'motivo')
    date_hierarchy = 'fecha_movimiento'
    
    
    
   # def save_model(self, request, obj, form, change):
        #super().save_model(request, obj, form, change)
        #for salida_producto in obj.salidaproducto_set.all():
       #     producto = salida_producto.producto
      #      producto.stock -= salida_producto.cantidad
     #       producto.save()

    #def delete_model(self, request, obj):
        # Evitar la modificación del stock al eliminar una salida
        #obj.delete()
   
#     def export_selected_to_pdf(modeladmin, request, queryset):
     
#          response = HttpResponse(content_type='application/pdf')
#          response['Content-Disposition'] = 'attachment; filename="Movimientos.pdf"'

#          p = canvas.Canvas(response, pagesize=(595, 842))  # Tamaño A4

#          pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
#          pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
         
#          p.setFont("Arial-Bold", 12)
#          p.drawString(100, 750, "Listas de movimientos")
#          p.setFont("Arial", 12)
#          y = 720
#          for item in queryset:
#             p.drawString(120, y, f"Movimiento: {item.id_Movimiento}")
#             p.drawString(120, y - 20, f"Tipo: {item.tipo}")
#             p.drawString(120, y - 40, f"Producto: {item.id_producto}")
#             p.drawString(120, y - 80, f"Paciente: {item.id_Paciente}")
#             y -= 120
#          p.showPage()
#          p.save()
#          return response

#     export_selected_to_pdf.short_description = "Exportar Movimientos seleccionados a PDF"
#     actions = [export_selected_to_pdf]
# admin.site.register(Movimiento,MovimientoAdmin)
admin.site.register(Entrada,EntradaAdmin)
admin.site.register(Salida,SalidaAdmin)
admin.site.register(AjusteStock, AjusteStockAdmin)
admin.site.register(HistorialMovimiento, HistorialMovimientoAdmin)
