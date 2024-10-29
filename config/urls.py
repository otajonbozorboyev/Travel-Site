from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.base.urls")),
    path('about/', include("apps.about.urls")),
    path('blog/', include("apps.blog.urls")),
    path('contact/', include("apps.contact.urls")),
    path('package/', include("apps.package.urls")),
    path('service/', include("apps.service.urls")),
    path('pages/', include("apps.pages.urls")),

] + debug_toolbar_urls()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def handler_404_view(request, *args, **kwargs):
    return render(request, '404.html', status=404)

handler404 = handler_404_view
