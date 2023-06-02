from django.contrib import admin

from .models import Category,Post
# Register your models here.


# Configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','url','add_date','image_tag')
    search_fields = ('title',)
admin.site.register(Category, CategoryAdmin)


# Configuration of Post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50
    
    class Media:
        # First src is the src of tinymce and second src is the js script path
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)
        
admin.site.register(Post,PostAdmin)