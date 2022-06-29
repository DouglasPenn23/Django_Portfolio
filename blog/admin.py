from django.contrib import admin
# Import Models you want to register on admin page
from blog.models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

# Register the models with the admin classes
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)