from blog.models import Category, Tag


def sidebar_context(request):
    return {
        'categories': get_categories(request),
        'tags': get_tags(request),
        'author': get_author(request),
        'sort': get_sort(request),
    }


def get_categories(request):
    return [c for c in Category.objects.all()]


def get_tags(request):
    return [t for t in Tag.objects.all()]


def is_tag_selected():
    pass


def get_author(request):
    pass


def get_sort(request):
    pass
