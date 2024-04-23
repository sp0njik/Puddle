from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from puddle import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
