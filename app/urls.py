from django.urls import path, re_path
from app import views
from buscamascota import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [
    path('', views.index, name='index'),
    path('colaborar/', views.colaborate, name='colaborar'),
    path('map/<int:page>', views.map, name='map'),
    path('map/', views.map, name='map'),
    path('publicar/', views.publish, name='publicar'),
    path('terminos/', views.terms, name='terminos'),
    path('licencia/', views.license, name='licencia'),
    path('exito/<int:report_id>', views.success, name='success'),
    re_path(r'^reporte/(?P<report_id>[0-9]+)$', views.report, name='report'),

    #API
    path('api/reportes/', views.ReportListAPI, name='report_list_json'),
    path('api/reportes/<int:page>', views.ReportListAPI, name='report_list_json_pages'),
    path('api/reportes/this-year', views.ReportListThisYearAPI, name='report_list_json_this_year')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)