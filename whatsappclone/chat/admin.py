import csv
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from django.contrib import admin
from django.http import HttpResponse
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

def convert_author_names_lowercase(modelAdmin, request, queryset):
    for post in queryset:
        post.author = str(post.author.lower())
        post.save()

def export_to_csv(modelAdmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['content-Disposition'] =  'attachment; filename="posts.csv"'
    writer = csv.writer(response)
    writer.writerow(['Author', 'Content', 'Pub_time', 'Price'])
    posts = queryset.values_list('author', 'content', 'pub_time', 'price')
    for post in posts:
        writer.writerow(post)
    return response

def export_to_pdf(modelAdmin, request, queryset):
    file_name = 'database.pdf'
    title = 'Post data'
    posts = queryset.values_list('author', 'content', 'pub_time', 'price')
    pdf = canvas.Canvas(file_name)
    pdf.setTitle(title)
    text = pdf.beginText(10, 10)
    text.setFont("Courier", 18)
    for post in posts:
        text.textLine(str(post))
    pdf.drawText(text)
    pdf.save()
    


# show this description in admin panel
apply_default_price.short_description = 'add default price'
convert_author_names_uppercase.short_description = 'convert author name to uppercase'
convert_author_names_lowercase.short_description = 'convert author name to lowercase'
export_to_csv.short_description = 'Export to CSV'
export_to_pdf.short_description = 'Save as PDF'




class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'pub_time', 'price']
    actions = [apply_default_price, convert_author_names_uppercase, convert_author_names_lowercase, export_to_csv , export_to_pdf]

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Post, PostAdmin)
admin.site.register(PostNotification)
