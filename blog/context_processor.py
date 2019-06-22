from blog.models import Category, Tag


def sidebar_context(request):
    return {
        'categories': get_categories(),
        'tags': get_tags(),
    }


def get_categories():
    return Category.objects.all()


def get_tags():
    return Tag.objects.all()
