# coding: utf-8
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView
from rest_framework.authtoken import views as drf_views

admin.site.site_header = _("GlobiFMV")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='fmv/login.html')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    # Django REST Framework
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', drf_views.obtain_auth_token, name='token'),
    # Fallout RPG
    path('', include('fmv.urls', namespace='fmv')),
    path('api/', include('fmv.api', namespace='fmv-api')),
]

# Common framework
if 'common' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('common/', include('common.urls', namespace='common')),
        path('api/common/', include('common.api.urls', namespace='common-api'))]

# Debug
if settings.DEBUG:
    # Static and media files
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Django Debug Toolbar
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns += [path('debug/', include(debug_toolbar.urls))]
