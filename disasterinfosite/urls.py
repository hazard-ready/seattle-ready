from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.gis import admin
from django.conf import settings
from django.contrib.auth import login, logout

from disasterinfosite import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('accounts/login/$', login),
   path('accounts/logout/$', logout),
   path('accounts/create_user/$', views.create_user),
   path('accounts/update_profile/$', views.update_profile),
   path('i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(path('$', views.app_view, name='index'))
urlpatterns += i18n_patterns(path('accounts/login/$',  login))
urlpatterns += i18n_patterns(path('accounts/logout/$', logout))
urlpatterns += i18n_patterns(path('accounts/create_user/$', views.create_user))
urlpatterns += i18n_patterns(path('accounts/update_profile/$', views.update_profile))

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
