from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import render
from app.models import Menu


class MenuListView(ListView):
    model = Menu
    template_name = 'index.html'
    context_object_name = 'menu'
    queryset = Menu.objects.filter(parent_id=None)


class MenuView(View):

    def get(self, request, *args, **kwargs):
        menu_slug = kwargs.get('menu_slug')
        menu_path = kwargs.get('menu_path')

        return render(
            request,
            'catalog.html',
            {'menu_slug': menu_slug, 'menu_path': menu_path})
