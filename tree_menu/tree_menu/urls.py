from django.contrib import admin
from django.urls import path
from app.views import MenuListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MenuListView.as_view(), name='menu_list')
]
