from re import search
from django.contrib import admin
from . models import Category,Post



# for config of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','cat_id','title','url','add_date',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display=('post_id','title','category','url',)
    search_fields=('title',)
    list_filter=('category',)
    list_per_page=(20)
    class Media:
        js=("js/script.js",)

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)

