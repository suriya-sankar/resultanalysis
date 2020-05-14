
from django.contrib import admin
from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.index,name='index'),
    path('add_batches/',views.add_batches,name='add_batches'),
    path('add_pdf/(?P<val3>[\w]+)/(?P<batch_name>[\w]+)/(?P<batch_id>\d+)/(?P<sem_id>\d+)/',views.add_pdf,name='add_pdf'),
    path('semester_list/(?P<batch_id>[\d]+)/',views.semester_list,name='semester_list'),
    # path('sem_result_display/(?P<data>\w+)/',views.sem_result_display,name='sem_result_display'),
    path('individual_page/(?P<row_n>\w+)/(?P<batch_id>\w+)/',views.individual_page,name='individual_page'),
    path('upload_pdf/',views.upload_pdf,name='upload_pdf'),
    path('reevalutation_upload/(?P<batch_id>\w+)/(?P<sem_id>\d+)/(?P<batch_name>\w+)/',views.reevalutation_upload,name='reevalutation_upload'),
    

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)