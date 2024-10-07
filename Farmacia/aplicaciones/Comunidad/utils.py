import matplotlib.pyplot as plt
from django.http import HttpResponse
import matplotlib.pyplot as io
import matplotlib.pyplot as base64
from aplicaciones.Comunidad.models import Empleado

def generar_grafico_distribucion_empleados(request):
 
  # Obtenemos los datos.
  empleados = Empleado.objects.all()
  puestos_trabajo = [empleado.trabajo for empleado in empleados]

  # Generamos el gráfico.
  plt.bar(puestos_trabajo, [puestos_trabajo.count(puesto) for puesto in puestos_trabajo])

  # Ajustamos el gráfico.
  plt.title("Distribución de empleados por puesto de trabajo")
  plt.xlabel("Puesto de trabajo")
  plt.ylabel("Número de empleados")

  # Guardamos el gráfico como un objeto base64.
  fig_bytes = io.BytesIO()
  plt.savefig(fig_bytes, format="png")
  fig_bytes.seek(0)

  # Devolvemos la respuesta HTTP con el gráfico.
  return HttpResponse(
    f"data:image/png;base64,{base64.b64encode(fig_bytes.read()).decode('utf-8')}",
    status=200,
  )
