from django import template
from app.models import Menu


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_slug: str):
    slugs = [slug for slug in context.request.path.split('/') if slug]
    menu_items = get_menu_items(menu_slug, slugs)
    menu_slugs = {item.slug: item for item in menu_items}

    for slug in slugs:
        parent = menu_slugs.get(slug)
        if parent:
            parent.children = [item for item in menu_items if item.parent_id == parent.id]

    menu = menu_slugs.get(menu_slug)
    parent_url = f'/{menu.slug}'
    set_urls(menu.children, parent_url)
    return {'menu': menu, 'submenu': menu.children}


def set_urls(tree, parent_url):

    def set_url(node):
        node.url = parent_url + '/' + node.slug
        if hasattr(node, 'children'):
            set_urls(node.children, node.url)

    list(map(set_url, tree))


def get_menu_items(menu_slug: str, slugs: list[str]):
    menu_items = Menu.objects.filter(slug=menu_slug)
    for slug in slugs:
        menu_items = menu_items | Menu.objects.filter(parent_id__slug=slug)
    return menu_items
