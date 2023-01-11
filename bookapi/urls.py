from django.contrib import admin
from django.urls import path, include
from django.http.response import HttpResponse
from django.conf.urls.static import static
from django.conf import settings


def index(request):
    return HttpResponse("Books Api")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ),
    path('books/', include('api.v1.books.urls', namespace='api_v1_books')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
