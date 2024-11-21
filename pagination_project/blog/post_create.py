from blog.models import Post

# Создание 15 записей через консоль джанго
for i in range(1, 16):
    Post.objects.create(
        title=f"Post {i}",
        content=f"Это пост номер  {i}.",
        created_at='2024-11-20 06:48:20'
    )

