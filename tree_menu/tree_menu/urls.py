from django.contrib import admin
from django.urls import path
from app.views import MenuListView, MenuView

from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = debug_toolbar_urls() + [
    path('admin/', admin.site.urls),
    path('', MenuListView.as_view(), name='menu_list'),
    path('<slug:menu_slug>/', MenuView.as_view()),
    path('<slug:menu_slug>/<path:menu_path>/', MenuView.as_view()),
]
