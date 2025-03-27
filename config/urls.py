from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls")),
    path("api/", include("api.urls")),
    path("accounts/", include("accounts.urls")),
    path("basket/", include("basket.urls")),
    path("orders/", include("orders.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
