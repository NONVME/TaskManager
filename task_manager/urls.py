from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include
from django.conf.urls import url


urlpatterns = i18n_patterns(
    url('admin/', admin.site.urls),
    url('', include('main.urls')),
    url('i18n/', include('django.conf.urls.i18n')),
)
