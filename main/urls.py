from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .settings import MEDIA_ROOT
from .views import *


urlpatterns = [
    path('', include('product.urls')),
    path('home/', HomePageView.as_view(), name='home_page_url'),
    path('admin/', admin.site.urls),
    path('account/', include('users.urls')),

]+static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
# +static(settings.STATIC.URL, document_root=STATIC_ROOT)

