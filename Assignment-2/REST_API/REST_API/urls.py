from django.contrib import admin
from django.urls import path
from app.views import userView, eventView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user', userView),
    path('api/event', eventView),
]
