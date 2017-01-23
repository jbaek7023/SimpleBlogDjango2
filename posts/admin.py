from django.contrib import admin

# Register your models here.
from .models import Post

class ModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]
    class Meta:
        model = Post
    
        

admin.site.register(Post, ModelAdmin)