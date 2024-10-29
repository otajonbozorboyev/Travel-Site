from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.base.urls")),
    path('about/', include("apps.about.urls")),
    path('blog/', include("apps.blog.urls")),
    path('contact/', include("apps.contact.urls")),
    path('package/', include("apps.package.urls")),
    path('service/', include("apps.service.urls")),
] + debug_toolbar_urls()
