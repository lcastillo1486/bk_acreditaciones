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
    path('templateMobil/',views.vistaMovil, name="vista_movil"),
    path('buscarPersonalMobil/',views.buscarPersonaMovil, name="buscar_personal_movil"),
    path('acreditacionMultiple/',views.acreditacionMultiple, name="acreditacion_multiple"),
    path('vistaSensei/',views.vistaSensei, name="vista_sensei"),
    path('scan/',views.vistaSensei, name="vista_sensei"),
    path('exportarExcel/<int:id>',views.exportarExcel, name="exportar_excel"),
    path('listadoEventos/',views.listadoEventos, name="listado_eventos"),
    path('importarBrazaletes/<int:id_evento>',views.importarBrazaletes, name="importar_brazaletes"),
    path('verEstado/<int:id_evento>',views.verEstado, name="ver_estado"),

]
