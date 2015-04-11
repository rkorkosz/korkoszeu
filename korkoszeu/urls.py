from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django.contrib.flatpages.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
