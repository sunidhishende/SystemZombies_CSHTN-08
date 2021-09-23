from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('', views.home, name="home"),
    path('video/<int:id>/',views.video, name="videos"),
    path('external/<int:id>/',views.external, name="external"),
    #path('sendresources', views.sendresources, name="sendresources"),
]

urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)