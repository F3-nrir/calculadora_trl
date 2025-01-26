"""
URL configuration for calculadora_trl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, messages
from django.urls import include, path, re_path, reverse 
from logica import urls
from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import views as auth_views

def make_messages(request):
    messages.add_message(request, messages.INFO, "Info message")
    messages.add_message(request, messages.ERROR, "Error message")
    messages.add_message(request, messages.WARNING, "Warning message")
    messages.add_message(request, messages.SUCCESS, "Success message")

    return HttpResponseRedirect(reverse("admin:index"))



urlpatterns = [
    #path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    #path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('calculadora/',include(urls), name="inicio"),
    path('i18n/', include('django.conf.urls.i18n')),
    path("make_messages/", make_messages, name="make_messages"),
]

urlpatterns += i18n_patterns(
    path('calculadora/admin/', admin.site.urls),
    path("calculadora/admin/password_reset/", auth_views.PasswordResetView.as_view(), name="admin_password_reset"),
    path("calculadora/admin/password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("calculadora/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("calculadora/reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
)