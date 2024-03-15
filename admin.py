from django.contrib import admin
from .models import Product,Category,SignUp, Size
# Register your models here.
# Register Category model
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display=('category_name',)
#Register product model
admin.site.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display=('product_image','product_detail','category','product_name','product_price')

# register my signup model here
@admin.register(SignUp)     
class AdminSignUp(admin.ModelAdmin):
    list_display=('first_name','last_name','phone_number','email','password')


@admin.register(Size)
class SizeModelAdmin(admin.ModelAdmin):
    list_display=("sizes",)