from django.contrib import admin

# Register your models here.


# um admin do django

from .models import Post

admin.site.register(Post)
