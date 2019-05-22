from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r"^uplaod/",views.new_image,name='upload'),
    url(r'^user/profile/',views.profile,name='profile'),
    url(r'user/edit/',views.edit_profile,name='edit'),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


