
from django.contrib import admin
from django.urls import path
from api.views import userView, itemView, bookingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user', userView),
    path('api/item', itemView),
    path('api/booking', bookingView),

]
