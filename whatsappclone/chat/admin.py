from django.contrib import admin
from .models import *
import decimal
# Register your models here.



#apply default price of $10.00
def apply_default_price(modelAdmin, request, queryset):
    for post in queryset:
        post.price = 10 * decimal.Decimal('0.9')
        post.save()

def convert_author_names_uppercase(modelAdmin, request, queryset):
    for post in queryset:
        post.author = str(post.author.upper())
        post.save()

def export_to_csv(modelAdmin, request, queryset):
    pass

# show this description in admin panel
apply_default_price.short_description = 'add default price'
convert_author_names_uppercase.short_description = 'convert author name to uppercase'



class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'pub_time', 'price']
    actions = [apply_default_price, convert_author_names_uppercase]

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Post, PostAdmin)
admin.site.register(PostNotification)
