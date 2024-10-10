from django.views.generic.list import ListView
from app.models import Menu


class MenuListView(ListView):
    model = Menu
    template_name = 'index.html'
    context_object_name = 'menu'
