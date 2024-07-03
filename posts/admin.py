from django.contrib import admin

from posts.models import *

# Register your models here.


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(LikeDislike)
