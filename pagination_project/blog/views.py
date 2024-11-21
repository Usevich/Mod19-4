from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from .models import Post


def post_list(request):
    post_list = Post.objects.all()
    per_page = request.GET.get('per_page', 5)  # Задаем количество на страницу, по умолчанию 5

    try:
        per_page = int(per_page)
        if per_page <= 0:
            per_page = 5
    except ValueError:
        per_page = 5

    paginator = Paginator(post_list, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'per_page': per_page}
    return render(request, 'blog/post_list.html', context)
