from django.contrib import admin

from post.models import PostImageModel, PostLikeModel, PostModel

# Register your models here.
admin.site.register(PostModel)
admin.site.register(PostLikeModel)
admin.site.register(PostImageModel)
