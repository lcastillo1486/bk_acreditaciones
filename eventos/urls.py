from django.urls import path
from eventos import views

urlpatterns = [
    path('eventos/',views.eventos, name="evento"),
    path('guardarEvento/',views.guardarEvento, name="guardar_evento"),
    path('importarExcel/<int:id_evento>',views.importarExcel, name="importar_excel"),
    path('iniciaAcreditacion/<int:id_evento>',views.iniciaAcreditacion, name="inicia_acreditacion"),
    path('detieneAcreditacion/<int:id_evento>',views.detieneAcreditacion, name="detiene_acreditacion"),
    path('descargaFormato/',views.descargaFormato, name="descarga_formato"),
    path('verMonitor/',views.verMonitor, name="ver_monitor"),
    path('acredPersonal/<int:id_reg>',views.acreditarPersonal, name="acred_personal"),
    path('buscarPersonal/',views.buscarPersona, name="buscar_personal"),
    path('registraUsuario/<int:cod_event>',views.registraUsuario, name="registra_usuario"),
]
